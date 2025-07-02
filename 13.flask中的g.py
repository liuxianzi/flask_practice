# -*- coding: utf-8 -*-
"""
 @Time           2025/7/2 18:11
 @File           13.flask中的g.py
 @Description    
 @Author         
"""
from flask import g
from flask import Flask


app = Flask(__name__)


@app.before_request
def f1():
    g.color = 'blue'


# 1.5
@app.route('/index')
def index():
    print(g.color)
    return 'okok'


@app.after_request
def f2(response):
    print(g.color)
    return response


if __name__ == '__main__':
    app.run()
