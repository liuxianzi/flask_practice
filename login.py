# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 20:50
 @File           login.py
 @Description    用户登录示例
 @Author         
"""
import functools
from flask import Flask, render_template, request, redirect, jsonify, url_for, session

app = Flask(__name__)
app.secret_key = 'zhelixiansuibianxie'  # 这里先随便写（其实按理是根据一个标准生成的

DATA_DICT = {
    '1': {'name': 'xiaoming', 'age': 18},
    '2': {'name': 'xiaodai', 'age': 19}
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # return jsonify({'name': 'xixi'})  # JsonResponse
        return render_template('login.html')  # render
    print(request.form)
    username = request.form.get('usr')
    password = request.form.get('pwd')
    if username == 'xiaoming' and password == '123':
        session[username] = 'record'  # session保存
        return redirect('/index')
    error = '用户名或密码错误'
    return render_template('login.html', error=error)


def auth(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        if session.get('xiaoming') != 'record':
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrap


@app.route('/index', endpoint='idx')  # endpoint相当于起别名的意思,不能重名 否则报错，若没声明endpoint，则默认别名是函数名
@auth
def index():
    return render_template('index.html', data=DATA_DICT)


@app.route('/edit', methods=['GET', 'POST'])
@auth
def edit():
    nid = request.args.get('nid')
    info = DATA_DICT[nid]
    if request.method == 'GET':
        return render_template('edit.html', info=info)
    else:
        name = request.form.get('username')
        age = request.form.get('age')
        info['name'] = name
        info['age'] = age
        return redirect(url_for('idx'))


@app.route('/del/<int:uid>')
@auth
def delete(uid):
    DATA_DICT.pop(str(uid))
    # url_for根据别名跳转
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run(debug=True)
