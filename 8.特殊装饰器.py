# -*- coding: utf-8 -*-
"""
 @Time           2025/6/29 17:26
 @File           8.特殊装饰器.py
 @Description    before_request,after_request
 @Author         
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.before_request
def func1():  # 无返回值，，加返回值会直接返回，不执行视图函数
    print('request before do something 1')


@app.before_request
def func2():
    print('request before do something 2')


@app.route('/index')
def index():
    print('hello')
    return 'hello'


@app.after_request
def func3(f):  # 必须接收参数，并返回。参数f其实就是视图函数执行后的返回值，这里 接收->处理 ->返回页面
    print('request after do something 1')
    return f


def func4(f):
    print('request after do something 2')
    return f


# 也可以这样写 和迭代器写法一样的作用
app.after_request(func4)


"""
可以有多个before_request和after_request
执行结果：
    request before do something 1
    request before do something 2
    hello
    request after do something 2
    request after do something 1

before_request的逻辑：先装进一个列表-》遍历-》执行
after_request的逻辑： 先装进一个列表——》reverse倒置-》遍历-》执行
"""

if __name__ == '__main__':
    app.run(debug=True)
