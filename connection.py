from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Muat file .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Variabel global untuk client dan db
client = None
db = None

def connect_to_mongodb():
    global client, db
    try:
        mongo_url = os.getenv('MONGODB_URL')
        client = MongoClient(mongo_url)
        db = client[os.getenv('DB_NAME')]
        print('Berhasil terhubung ke MongoDB')
    except Exception as e:
        print(f"Terjadi kesalahan dalam koneksi MongoDB: {e}")

connect_to_mongodb()

def get_collection(collection_name):
    return db[collection_name]