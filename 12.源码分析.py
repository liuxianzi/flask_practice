# -*- coding: utf-8 -*-
"""
 @Time           2025/7/1 20:56
 @File           12.源码分析.py
 @Description    flask源码分析
 @Author         
"""
from flask import Flask

# 1.1
app = Flask(__name__)
# 1.2
app.config.from_object('settings.py')


# 1.3
@app.before_request
def f1():
    print('before do')


# 1.4
@app.after_request
def f2(response):
    return response


# 1.5
@app.route('/index')
def index():
    return 'okok'


# 1.6
if __name__ == '__main__':
    app.run()
