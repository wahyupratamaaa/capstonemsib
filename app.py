
from flask import Flask,render_template
from server_admin import admin_blueprint
from server_user import user_blueprint
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.getenv('SECRET_KEY')

app = Flask(__name__)
app.secret_key = SECRET_KEY 

app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(user_blueprint, url_prefix='/user')

print('-' * 50, 'app.py', '-' * 50)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ruangdeveloper")
def tentang():
    return render_template("dev/ruangdeveloper.html")

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)
