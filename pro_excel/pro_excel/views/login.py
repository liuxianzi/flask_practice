# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 15:50
 @File           login.py
 @Description    session判断登录权限
 @Author         
"""
from flask import Blueprint, render_template, request, session, redirect
from ..common.sqlhelper import db


sess = Blueprint('sess', __name__)


@sess.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('usr')
    password = request.form.get('pwd')
    # 先建表
    sql = "show tables like 'user'"
    ret = db.execute(sql)
    if not ret:
        sql = 'create table user(id bigint auto_increment primary key,name varchar(50) not null , ' \
              'pwd varchar(200), is_login tinyint(1) not null)'
        db.execute(sql)
    # 存缓存，写数据表
    is_session = session.get(username)
    if not is_session:
        session[username] = 'log in'
        if db.fetchone('select * from user where name=%s', username):
            return redirect(f'/home?name={username}')
        sql = """insert into user(name, pwd, is_login) values (%s, %s, %s)"""
        try:
            db.execute(sql, username, password, 1)
            return redirect(f'/home?name={username}')
        except Exception as e:
            print('插入失败:', e)
            return render_template('login.html')
    else:
        return redirect(f'/home?name={username}')


@sess.route('/home')
def home():
    username = request.args.get('name')
    if session.get(username) == 'log in':
        return f'欢迎来到 {username} 主页'
    return redirect('/login')
