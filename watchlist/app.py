from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db = SQLAlchemy(app)

@app.route('/')
def index():
    name = "元斌"
    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"战狼","year":"2015"},
        {"title":"战狼2","year":"2018"},
        {"title":"囧妈","year":"2020"},
        {"title":"叶问","year":"2019"},
        {"title":"杀破狼","year":"2017"},
        {"title":"极限特工","year":"2016"},
        {"title":"疯狂外星人","year":"2018"},
    ]
    return render_template("index.html",name=name,movies=movies)