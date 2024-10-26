from flask import Flask, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")  

@app.route("/job")
def job():
    url = "https://my-json-server.typicode.com/jjjosephhh/test-db-002/people"
    r = requests.get(url)
    rows = r.json()
    return render_template("job.html", rows = rows)

if __name__ == "__main__":
    try:
        app.run('0.0.0.0', port=3000, debug=True)
    except Exception as e:
        print("Terjadi kesalahan saat menjalankan aplikasi:", e)
