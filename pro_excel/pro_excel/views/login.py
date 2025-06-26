# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 15:50
 @File           login.py
 @Description    session判断登录权限
 @Author         
"""
from flask import Blueprint, render_template, request, session, redirect
from ..common.db_cursor import conn, create_table


sess = Blueprint('sess', __name__)


@sess.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('usr')
    password = request.form.get('pwd')
    db, cursor = conn()
    # 先建表
    sql = "show tables like 'user'"
    ret = cursor.execute(sql)
    if not ret:
        sql = 'create table user(id bigint auto_increment primary key,name varchar(50) not null , ' \
              'pwd varchar(200), is_login tinyint(1) not null)'
        create_table(cursor, sql)
    # 存缓存，写数据表
    session[username] = 'log in'
    sql = """insert into user(name, pwd, is_login) values ('%s', '%s', '%d')""" % (username, password, 1)
    try:
        cursor.execute(sql)
        db.commit()
        return redirect(f'/home?name={username}')
    except Exception as e:
        print('插入失败:', e)
        db.rollback()
        return render_template('login.html')


@sess.route('/home')
def home():
    print(request.args)
    username = request.args.get('name')
    if session.get(username) == 'log in':
        return f'欢迎来到 {username} 主页'
    return redirect('/login')
