from watchlist import app,db
from flask_login import login_user,logout_user,login_required,current_user
from flask import Flask,url_for,render_template,request,redirect,flash
from watchlist.models import User,Movie
import click

#view 视图函数
@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
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
@login_required
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
@app.route('/movie/delete/<int:movie_id>',methods=['POST','GET'])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除完成')
    return redirect(url_for('index'))

#自定义指令，生成管理账号，输入用户名密码，确认密码
@app.cli.command()
@click.option('--username',prompt=True,help='登录用户名')
@click.option('--password',prompt=True,help='密码',confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新用户管理员')
        user.username = username
        user.set_password(password) 
    else:
        click.echo('创建管理员账户')
        user = User(username=username,name='元斌')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('管理员账号更新/创建完成')

#登录
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('输入有误')
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('登陆成功')
            return redirect(url_for('index'))
        flash('验证失败')
        return redirect(url_for('login'))

    return render_template('login.html')

#登出logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('退出成功')
    return redirect(url_for('index'))

#设置
@app.route('/settings',methods=['POST','GET'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if not name or len(name)>20:
            flash('输入有误')
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash('名字更新完成')
        return redirect(url_for('index'))

    return render_template('settings.html')