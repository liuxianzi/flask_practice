# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 19:55
 @File           werkzeug_.py
 @Description    flask底层就是基于werkzeug的wsgi实现的,,了解wsgi底层的实现
 @Author         
"""
from werkzeug.serving import run_simple

"""实现1"""
# def func(environ, start_response):
#     print('服务被启动了')
#
#
# run_simple('127.0.0.1', 5000, func)
#

"""实现2"""
class Flask(object):
    def __call__(self, environ, start_response):
        return 'hello world （run_simple输出的'

    def run(self):
        run_simple('127.0.0.1', 5000, self)

app = Flask()


if __name__ == '__main__':
    app.run()

"""方法2之前是可以成功运行起来的，现在不可以了，，但是原理就是如此"""

