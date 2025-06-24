# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 20:50
 @File           login.py
 @Description    用户登录示例
 @Author         
"""
from flask import Flask, render_template, request, redirect, jsonify, url_for

app = Flask(__name__)

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
        return redirect('/index')
    error = '用户名或密码错误'
    return render_template('login.html', error=error)


@app.route('/index', endpoint='idx')  # endpoint相当于起别名的意思
def index():
    return render_template('index.html', data=DATA_DICT)


@app.route('/edit')
def edit():
    nid = request.args.get('nid')
    print(DATA_DICT[nid])
    DATA_DICT[nid]['age'] += 1
    return redirect(url_for('idx'))


@app.route('/del/<int:uid>')
def delete(uid):
    DATA_DICT.pop(str(uid))
    # url_for根据别名跳转
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run(debug=True)
