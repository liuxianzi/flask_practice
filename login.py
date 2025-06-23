# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 20:50
 @File           login.py
 @Description    用户登录示例
 @Author         
"""
from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # return jsonify({'name': 'xixi'})  # JsonResponse
        return render_template('login.html')  # render
    print(request.form)
    username = request.form.get('usr')
    password = request.form.get('pwd')
    if username == 'xiaoming' and password == '123':
        return redirect('/index')
    error = '用户名或密码错误'
    return render_template('login.html', error=error)


@app.route('/index')
def index():
    return '首页'


if __name__ == '__main__':
    print(app.route)
    app.run(debug=True)
