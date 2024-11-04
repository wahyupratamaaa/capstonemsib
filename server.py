
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

# MONGODB_URL = os.getenv('MONGODB_URL')
# DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)

try:
    # client = MongoClient(MONGODB_URL)
    # db = client[DB_NAME]
    print("Koneksi ke MongoDB berhasil!")
except Exception as e:
    print(f"Gagal terhubung ke MongoDB: {e}")

@app.route("/")
def awal():
    return render_template("awal.html")

@app.route("/data")
def data():
    return render_template("data.html")
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
