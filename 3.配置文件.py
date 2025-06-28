# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 16:21
 @File           3.配置文件.py
 @Description    
 @Author         
"""
from flask import Flask

app = Flask(__name__)

# 引入配置文件
app.config.from_object('config.settings')


@app.route('/index')
def index():
    text = app.config.get('NAME')
    return text


if __name__ == '__main__':
    app.run(debug=True)
