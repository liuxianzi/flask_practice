# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 19:55
 @File           werkzeug_.py
 @Description    flask底层就是基于werkzeug的wsgi实现的,,了解wsgi底层的实现
 @Author         
"""

"""实现1"""
from werkzeug.serving import run_simple
from werkzeug.wrappers import Response


def func(environ, start_response):
    print('服务被启动了')
    response = Response("hello it's start")
    return response(environ, start_response)


run_simple('127.0.0.1', 5000, func)


"""实现2"""
"""
# from flask import Flask
from flask.wrappers import Response


class Fflask(object):

    def __call__(self, environ, start_response):
        print('服务启动了')
        response = Response('hello')
        return response(environ, start_response)

    def run(self):
        run_simple('127.0.0.1', 5000, self)


app = Fflask()


if __name__ == '__main__':
    app.run()
"""