# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 18:30
 @File           4.路由.py
 @Description    路由相关
 @Author         
"""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

"""路由实现的2种方法：
       ①迭代器 
       ②add_url_rule
"""


@app.route('/index1')
def index1():
    return 'ok'


def index2():
    return 'okk'


app.add_url_rule('/index2', endpoint='index2', view_func=index2)


@app.route('/index3/<name>')
def index3(name):
    print(type(name))  # str
    return 'index3'


@app.route('/index4/<int:name>')  # <int:name> 会自动将name参数的值转为int型
def index4(name):
    print(type(name))  # int
    return 'index4'


"""自定义正则路由"""


class RegexConverter(BaseConverter):
    def __init__(self, map, regex):
        super().__init__(map)
        self.regex = regex


app.url_map.converters['regex'] = RegexConverter


@app.route('/index5/<regex("\d{3}"):name>')  # name参数值 只能为3位数，否则404
def index5(name):
    print(name)
    print(type(name))  # int
    return 'index5'


if __name__ == '__main__':
    app.run()
