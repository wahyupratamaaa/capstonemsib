from flask import Flask, Blueprint, render_template, request, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from connection import db
# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv(dotenv_path)
# load_dotenv()


# MONGODB_URL = os.getenv('MONGODB_URL')
# DB_NAME = os.getenv('DB_NAME')

# client = MongoClient(MONGODB_URL)
# db = client[DB_NAME]

user_blueprint = Blueprint('user', __name__, template_folder='templates')

@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()  
        print('Data Toko', data)
        username = data.get("username")
        password = data.get("password")
        
        user = db.Pengguna.find_one({"username": username})

        if user and check_password_hash(user["password"], password):

            return jsonify({"message": f"Hi Selamat Datang "}), 200
        else:
            return jsonify({"error": "Username atau password salah"}), 401
    return render_template("clients/login.html")


@user_blueprint.route("/registrasi", methods=["GET", "POST"])
def registrasi():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmmpassword = request.form.get("confirmmpassword")

        if not username or not password or not confirmmpassword:
            return jsonify({"error": "Semua field harus diisi"}), 400
        if password != confirmmpassword:
            return jsonify({"error": "Password dan konfirmasi password tidak cocok"}), 400

        hashed_password = generate_password_hash(password)

        user_data = {
            "username": username,
            "password": hashed_password,
            "created_at": datetime.now()
        }

        db.Pengguna.insert_one(user_data)
        return jsonify({"message": "Registrasi berhasil!"}), 201

    return render_template("clients/registrasi.html")

@user_blueprint.route("/logout")
def logout():
    return render_template('/templates/index.html')


@user_blueprint.route("/dashboard")
def dashboard():
        return render_template("clients/dashboard.html")

@user_blueprint.route("/produk")
def produk():
    return render_template("clients/produk.html")


@user_blueprint.route("/checkout")
def checkout():
    return render_template("clients/checkout.html")

@user_blueprint.route("/dashboardProduk")
def dashboardProduk():
    return render_template("clients/dashboardProduk.html")

@user_blueprint.route("/kontak")
def kontak():
    return render_template("clients/kontak.html")


@user_blueprint.route("/dashboardPenjual")
def dashboardPenjual():
    return render_template("clients/dashboardPenjual.html")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix='/user')
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)