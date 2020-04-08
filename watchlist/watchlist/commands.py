import click
from watchlist import db,app
from watchlist.models import User,Movie

#自定义命令
@app.cli.command()   #把以下内容注册为命令
@click.option('--drop',is_flag=True,help="先删除后创建")  
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("初始化成功")


