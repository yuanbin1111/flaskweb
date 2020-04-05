import os,sys

from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
import click

WIN = sys.platform.startswith('win')
if WIN:
    perfix = 'sqlite:///'   #window平台
else:
    perfix = 'sqlite:////'  #Mac Linux平台

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = perfix + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))



#view 视图函数
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

#自定义命令
@app.cli.command()   #把以下内容注册为命令
@click.option('--drop',is_flag=True,help="先删除后创建")  
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化成功")


#自定义错误页面
@app.errorhandler(404)
def page_not(a):
    user = User.query.first()
    return render_template('404.html',user=user)