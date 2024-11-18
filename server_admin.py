from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.getenv('MONGODB_URL')
DB_NAME = os.getenv('DB_NAME')
SECRET_KEY = os.getenv('SECRET_KEY')

client = MongoClient(MONGODB_URL)
db = client[DB_NAME]

UPLOAD_FOLDER = 'static/uploads'

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


admin_blueprint = Blueprint('admin', __name__, template_folder='templates')

@admin_blueprint.route("/login_server", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        user = db.Toko.find_one({"username": username})

        if user and check_password_hash(user["password"], password):
            session["user_id"] = str(user["_id"])
            session["username"] = user["username"]

            return jsonify({"message": f"Hi , Selamat Datang "}), 200
        else:
            return jsonify({"error": "Username atau password salah"}), 401

    return render_template("server/login_server.html")


@admin_blueprint.route("/registrasi_server", methods=["GET", "POST"])
def registrasi():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if not username or not password or not confirm_password:
            return jsonify({"error": "Semua field harus diisi"}), 400
        if password != confirm_password:
            return jsonify({"error": "Password dan konfirmasi password tidak cocok"}), 400

        hashed_password = generate_password_hash(password)

        user_data = {
            "username": username,
            "password": hashed_password,
            "created_at": datetime.now()
        }

        db.Toko.insert_one(user_data)
        return jsonify({"message": "Registrasi EduBooks MarketPlace berhasil!"}), 201

    return render_template("server/registrasi_server.html")


@admin_blueprint.route("/dashboard_toko", methods=['GET', 'POST'])
def dashboardPenjual():
    try:
        if "username" not in session:
            return redirect(url_for('admin.login'))
        
        if request.method == 'POST':
            penulis_receive = request.form.get('penulis_give')
            judul_receive = request.form.get('judul_give')
            harga_receive = request.form.get('harga_give')

            if 'file_give' not in request.files:
                return jsonify({'error': 'Tidak ada file yang diunggah'}), 400

            file = request.files['file_give']
            harga_receive = int(harga_receive)

            if file and allowed_file(file.filename):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = secure_filename(f"{file.filename.rsplit('.', 1)[0]}-{timestamp}.{file.filename.rsplit('.', 1)[-1]}")
                filepath = os.path.join(UPLOAD_FOLDER, filename)


                
                file.save(filepath)

            else:
                return jsonify({'error': 'Format file tidak didukung'}), 400
            # count = db.books.count_documents({})
            # num = count + 1
            
            doc = {
                'penulis': penulis_receive,
                'judul': judul_receive,
                'harga': harga_receive,
                'image': filename,
                # "num" : num,
                # "done" : 0
            }

            db.books.insert_one(doc)

            print(f"Data berhasil disimpan: {doc}")
            return jsonify({'msg': 'Data buku berhasil disimpan!'}), 200

        return render_template("server/dashboard_toko.html", username=session["username"])

    except Exception as e:
        print(f"Error saat menyimpan data: {e}")
        return jsonify({'error': 'Terjadi kesahalan dalam menyimpan data'}), 500

@admin_blueprint.route("/logout")
def logout():
    session.clear() 
    return redirect(url_for('admin.login'))


@admin_blueprint.route("/dashboard_server")
def dashboard():
    if "user_id" in session:
        return render_template("server/dashboard_server.html", username=session["username"])
    return redirect(url_for('login.server'))


@admin_blueprint.route("/produk_server", methods=["GET"])
def produk():
    books = list(db.books.find({}, {'_id': False}))
    for book in books:
        book['image'] = url_for('static', filename=f'uploads/{book["image"]}')
    print("Books:", books)
    # return jsonify(books), 200

    # return render_template("server/produk_server.html", books=books)

    return render_template("server/produk_server.html")

@admin_blueprint.route("/checkout")
def checkout():
    return render_template("clients/checkout.html")

@admin_blueprint.route("/dashboardProduk")
def dashboardProduk():
    return render_template("clients/dashboardProduk.html")

@admin_blueprint.route("/kontak")
def kontak():
    return render_template("clients/kontak.html")


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    return app

# Menjalankan aplikasi Flask
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
