import os,sys

from flask import Flask,url_for,render_template,request,redirect,flash
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
app.config['SECRET_KEY'] = '1903_dev'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))



#view 视图函数
@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        #获取表单数据
        title = request.form.get('title')
        year = request.form.get('year')
        #验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash("输入错误")
            return redirect(url_for('index'))
        #如果条件都满足，就将数据保存到数据库
        movie = Movie(title=title,year=year)  #创建记录
        db.session.add(movie)
        db.session.commit()
        flash("添加数据成功")
        return redirect(url_for('index'))
    movies = Movie.query.all()
    return render_template("index.html",movies=movies)


#更新修改
@app.route('/movie/edit/<int:movie_id>',methods=['POST','GET'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入有误')
            return redirect(url_for('edit',movie_id=movie_id))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('电影更新完成')
        return redirect(url_for('index'))
    return render_template('edit.html',movie=movie)

#删除

#更新修改
@app.route('/movie/delete/<int:movie_id>',methods=['POST','GET'])
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除完成')
    return redirect(url_for('index'))


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