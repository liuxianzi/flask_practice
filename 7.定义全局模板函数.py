# -*- coding: utf-8 -*-
"""
 @Time           2025/6/29 00:30
 @File           7.定义全局模板函数.py
 @Description    
 @Author         
"""
from flask import Flask, render_template

app = Flask(__name__)


# 方式1，更常用
@app.template_global()
def test(args):
    return 'test' + args


# 方式2
@app.template_filter()
def test2(args):  # 在模板中引用：{{ '哈哈'|test2() }}  其中 哈哈就相当于test2的第一个参数(第一个参数值必须用这个方法写，否则报错)；
    # 允许有多个参数，剩余参数按之前的写，eg:{{ '哈哈'|test2(参数2，参数3，...) }}
    return 'test2' + args


@app.route('/mb/global')
def index():
    books = ['或者', '活着']
    return render_template('mb_global.html', books=books)  # 可以传变量，也可以传函数给模板


if __name__ == '__main__':
    app.run()
