# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 19:55
 @File           werkzeug_.py
 @Description    flask底层就是基于werkzeug的wsgi实现的,,了解wsgi底层的实现
 @Author         
"""
from flask.globals import request_ctx
from werkzeug.serving import run_simple

"""实现1"""
# def func(environ, start_response):
#     print('服务被启动了')
#
#
# run_simple('127.0.0.1', 5000, func)
#

from flask import Flask
from flask.wrappers import Response
"""实现2"""


class Flask(object):

    response_class: type[Response] = Response

    def make_default_options_response(self):
        """This method is called to create the default ``OPTIONS`` response.
        This can be changed through subclassing to change the default
        behavior of ``OPTIONS`` responses.

        .. versionadded:: 0.7
        """
        # adapter = request_ctx.url_adapter
        # methods = adapter.allowed_methods()  # type: ignore[union-attr]
        rv = self.response_class()
        # rv.allow.update(methods)
        return rv

    def __call__(self, environ, start_response):
        print('服务启动了')
        return self.make_default_options_response()

    def run(self):
        run_simple('127.0.0.1', 5000, self)

app = Flask()


if __name__ == '__main__':
    app.run()

"""方法2之前是可以成功运行起来的，现在不可以了，，但是原理就是如此"""

