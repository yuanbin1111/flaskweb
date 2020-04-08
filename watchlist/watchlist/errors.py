from watchlist import app
from flask import render_template

#自定义错误页面
@app.errorhandler(404)
def page_not(a):
    return render_template('404.html')