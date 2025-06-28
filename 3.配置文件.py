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
# 方式1：基于全局变量
# app.config.from_object('config.settings')
# 方式2：基于类的方式
# app.config.from_object('config.allsettings.ProdSettings')
# app.config.from_object('config.allsettings.TestSettings')
app.config.from_object('config.allsettings.LocalSettings')


@app.route('/index')
def index():
    text = app.config.get('NAME')
    return text


if __name__ == '__main__':
    app.run(debug=True)
