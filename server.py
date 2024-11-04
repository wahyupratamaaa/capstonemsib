
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from os.path import join, dirname
from datetime import datetime
import requests
# from bs4 import BeautifulSoup
# print('scraping success bs4' )


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URL = os.getenv('MONGODB_URL')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)

try:
    client = MongoClient(MONGODB_URL)
    db = client[DB_NAME]
    print("Koneksi ke MongoDB berhasil!")
except Exception as e:
    print(f"Gagal terhubung ke MongoDB: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book", methods=["POST"])
def book():
    jenis_kendaraan = request.form.get("jenis_kendaraan")
    merek = request.form.get("merek")
    nomor_plat = request.form.get("nomor_plat")

    if not all([jenis_kendaraan, merek, nomor_plat]):
        return jsonify({"msg": "Data tidak lengkap"}), 400

    try:
        db.books.insert_one({
            "jenis_kendaraan": jenis_kendaraan,
            "merek": merek,
            "nomor_plat": nomor_plat,
            "tanggal_input": datetime.now()
        })
        return jsonify({"msg": "Data berhasil disimpan!"}), 200
    except Exception as e:
        return jsonify({"msg": f"Gagal menyimpan data: {e}"}), 500

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/awal")
def awal():
    # url = "https://www.gramedia.com/"
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # }
    # response = requests.get(url, headers=headers)

    # if response.status_code == 200:
    #      soup = BeautifulSoup(response.text, "html.parser")
    return render_template("awal.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/registrasi")
def registrasi():
    return render_template("registrasi.html")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
@app.route("/produk")
def produk():
    return render_template("produk.html")

if __name__ == "__main__":
    app.run('0.0.0.0', port=3080, debug=True)
