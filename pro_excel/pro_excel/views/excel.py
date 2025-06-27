# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 16:42
 @File           excel.py
 @Description    上传excel文件，并展示其中内容
 @Author         
"""
import os
import pandas as pd
from flask import Blueprint, render_template, request, redirect
from ..common.sqlhelper import db


books = Blueprint('upload', __name__)


@books.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'GET':
        """读取所有数据库的书籍数据"""
        sql = 'select * from book;'
        rets = db.fetchall(sql)
        return render_template('book.html', books=rets)

    file = request.files.get('upload_file')
    if not file:
        return render_template('book.html')
    """ 存储文件 """
    filename = file.filename
    file_path = os.path.join('pro_excel/upload/', filename)
    file.save(file_path)
    """ 读取文件数据 写入数据表book """
    # 读数据
    df = pd.read_excel(os.path.join(os.getcwd(), file_path))
    datas = df.values.tolist()  # 获取所有数据在一个列表中
    # 写入数据
    sql = "show tables like 'book'"
    ret = db.execute(sql)
    if not ret:
        sql = 'create table book(id bigint auto_increment primary key, title varchar(50) not null , ' \
              'author varchar(200) not null , price int default null)'
        _ = db.execute(sql)
    sql = f"""insert into book(title, author, price) value(%s, %s, %s)"""
    try:
        _ = db.execute_many(sql, datas)
    except Exception as e:
        print('插入数据出错：', e)
    return redirect(request.url)


@books.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add_book.html')
    title = request.form.get('title')
    author = request.form.get('author')
    price = request.form.get('price')

    sql = """insert into book(title,author,price) values (%s,%s,%s)"""
    db.execute(sql, title, author, price)
    return redirect('/book')


@books.route('/update', methods=['GET', 'POST'])
def update():
    bid = int(request.args.get('bid'))
    if request.method == 'GET':
        sql = """select * from book where id=%s"""
        ret = db.fetchone(sql, bid)
        return render_template('edit_book.html', ret=ret)

    title = request.form.get('title')
    author = request.form.get('author')
    price = request.form.get('price')

    sql = """update book set title=%s,author=%s,price=%s where id=%s"""
    db.execute(sql, title, author, price, bid)
    return redirect('/book')


@books.route('/del')
def delete():
    bid = int(request.args.get('bid'))
    sql = """delete from book where id=%s"""
    db.execute(sql, bid)
    return redirect('/book')


if __name__ == '__main__':
    file_path = os.path.join('/'.join(os.getcwd().split('/')[:-2]), 'pro_excel/upload/book.xlsx')
    print(file_path)
    df = pd.read_excel(file_path)
    print(df)
    print(df.values.tolist(), type(df.values))
    # for index, row in df.iterrows():
    #     print(row.values.tolist(), type(row.values))
