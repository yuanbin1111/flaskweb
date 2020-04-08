import os,sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)


WIN = sys.platform.startswith('win')
if WIN:
    perfix = 'sqlite:///'   #window平台
else:
    perfix = 'sqlite:////'  #Mac Linux平台

app = Flask(__name__)
os.path.dirname(app.root_path)

app.config['SQLALCHEMY_DATABASE_URI'] = perfix + os.path.join(os.path.dirname(app.root_path),'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','.dev')



db = SQLAlchemy(app)
login_manager = LoginManager(app)  #实例化拓展类
from watchlist.models import User
@login_manager.user_loader

def load_user(user_id):  #创建用户加载回调函数，接受用户id作为参数
    user =User.query.get(user_id)
    return user

#如果没有登录而进行操作会返回到登录页面
login_manager.login_view = 'login'


#模板上下文处理函数
@app.context_processor
def common_user():
    from watchlist.models import User
    user =User.query.first()
    return dict(user=user)

from watchlist import views,errors,commands
