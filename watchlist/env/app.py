from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)

@app.route('/')
def index():
    return "首页"