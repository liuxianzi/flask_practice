# -*- coding: utf-8 -*-
"""
 @Time           2025/6/23 19:26
 @File           demo.py
 @Description    
 @Author         
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
