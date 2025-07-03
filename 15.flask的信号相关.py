# -*- coding: utf-8 -*-
"""
 @Time           2025/7/3 20:45
 @File           15.flask的信号相关.py
 @Description    
 @Author         
"""
from flask import Flask, render_template, signals, current_app, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'suiji'


class MyMiddleWare:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        print('在调用wsgi_app方法前执行')
        return self.wsgi_app(*args, **kwargs)


app.wsgi_app = MyMiddleWare(app.wsgi_app)


@signals.appcontext_pushed.connect
def f1(app):
    print('1.信号：在app_ctx被添加到上下文后执行')


@signals.request_started.connect
def f2(app):
    print('2.信号：在开始处理请求前执行')


@app.before_request
def f4():
    print('4.在执行视图函数之前执行')


@app.url_value_preprocessor
def f3(endpoint, args):
    print('3.在before_request执行之前运行')


@signals.before_render_template.connect
def f5(app, template, context):
    print('6.开始渲染模板前执行')


@signals.template_rendered.connect
def f6(app, template, context):
    print('7.模板渲染结束后执行')


@app.after_request
def f7(response):
    print('8.在执行视图函数之后执行')
    return response


@signals.request_finished.connect
def f8(app, response):
    print('9.在after_request执行之后执行')


@signals.request_tearing_down.connect
def f9(app, exc):
    print('10.在将ctx被pop出上下文前 执行的')


@signals.appcontext_tearing_down.connect
def f10(app, exc):
    print('11.在将app_ctx被pop出上下文前 执行的')
    print(current_app)


@signals.appcontext_popped.connect
def f11(app):
    print('12.在将app_ctx被pop出上下文之后 执行的')
    # print(current_app)  # 会报错的，因为此时app_ctx已经不在上下文里了


@app.route('/index')
def index():
    # flash 是依靠session实现的，所以必须设置secret_key
    flash('我是一次性消息，拿走就没了')
    print('5.模板渲染开始')
    return render_template('signal.html')


@app.route('/home')
def home():
    print(get_flashed_messages())
    return 'home'


if __name__ == '__main__':
    app.run(debug=True)
