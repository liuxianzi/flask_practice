# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 15:03
 @File           2.flask静态文件配置.py
 @Description    
 @Author         
"""
from flask import Flask, render_template

# static_folder 静态文件目录，static_url_path静态文件访问路由，，一般默认都是static，我们无需修改
app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/st')
def index():
    return render_template('st.html')


if __name__ == '__main__':
    app.run(debug=True)
