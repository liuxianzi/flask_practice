# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 15:41
 @File           __init__.py.py
 @Description    蓝图（blue print）项目
 @Author         
"""
from flask import Flask
from .views.login import sess
from .views.excel import books


def create_app():
    app = Flask(__name__)
    app.secret_key = 'xiansuibianxie'

    @app.route('/index')
    def index():
        return 'index'

    app.register_blueprint(sess)
    app.register_blueprint(books)
    # url_prefix 路由前缀，不加则表示无
    # app.register_blueprint(sess, url_prefix='/sess')
    return app
