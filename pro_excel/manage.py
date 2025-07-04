# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 15:42
 @File           manage.py
 @Description    
 @Author         
"""
from pro_excel import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
