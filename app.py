from flask import Flask,render_template
from server_admin import admin_blueprint
from server_user import user_blueprint
from connection import connect_to_mongodb
# from pymongo import MongoClient
# from dotenv import load_dotenv
# import os
# import logging

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# load_dotenv(dotenv_path)

# MONGODB_URL = os.getenv('MONGODB_URL')
# print('kamuu berjalan di ', MONGODB_URL)
connect_to_mongodb()
app = Flask(__name__)

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(user_blueprint, url_prefix='/user')

print('-' * 50, 'app.py', '-' * 50)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/footer')
def footer():
    return render_template("dev/footer.html")

@app.route("/ruangdeveloper")
def tentang():
    return render_template("dev/ruangdeveloper.html")
# @app.route("/dashboard_update")
# def dashboard_edit_produk():
#     return render_template("server/dashboard_edit.html")

if __name__ == "__main__":
    app.run('0.0.0.0', port=3000, debug=True)