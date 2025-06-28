# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 23:51
 @File           5.视图.py
 @Description    函数视图FBV+类视图CBV
 @Author         
"""
from flask import Flask, views

app = Flask(__name__)


# FBV(function based views) 函数视图
@app.route('/index')
def index():
    return 'index'


# CBV(class based views) 类视图
def test1(func):
    def wraps(*args, **kwargs):
        print('before1')
        ret = func(*args, **kwargs)
        print('after1')
        return ret
    return wraps


def test2(func):
    def wraps(*args, **kwargs):
        print('before2')
        ret = func(*args, **kwargs)
        print('after2')
        return ret
    return wraps


class UserView(views.MethodView):
    methods = ['GET', 'POST']  # 如果未定义methods，则默认get,post方法都可用；但是如果定义了，则只能接收定义在内的请求方式
    decorators = [test1, test2]  # 装饰器，可以添加多个；装饰器可以在函数执行前后做一些操作

    def get(self):
        print('get')
        return 'get'

    def post(self):
        print('post')
        return 'post'


app.add_url_rule('/user', view_func=UserView.as_view('user'))  # UserView.as_view('user') 其中的user就是endpoint


if __name__ == '__main__':
    app.run()
