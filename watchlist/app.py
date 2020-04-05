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
    movies = Movie.query.all()
    return render_template("index.html",movies=movies)

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
    return render_template('404.html')


#模板上下文处理函数
@app.context_processor
def common_user():
    user =User.query.first()
    return dict(user=user)