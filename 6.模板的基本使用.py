# -*- coding: utf-8 -*-
"""
 @Time           2025/6/29 00:18
 @File           6.模板的基本使用.py
 @Description    
 @Author         
"""
from flask import Flask, render_template

app = Flask(__name__)


def test(args):
    return 'test' + args


@app.route('/mb')
def index():
    books = ['或者', '活着', '火灾']
    return render_template('mb.html', books=books, func=test)  # 可以传变量，也可以传函数给模板


""" 问题：如果有多个视图返回模板想引入test函数，就都得在返回值里写明，有什么方法可以优化呢？"""


if __name__ == '__main__':
    app.run()
