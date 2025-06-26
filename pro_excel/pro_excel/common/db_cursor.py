# -*- coding: utf-8 -*-
"""
 @Time           2025/6/26 16:58
 @File           db_cursor.py
 @Description    
 @Author         
"""
import pymysql


def conn():
    db = pymysql.connect(
        user='root',
        password="",
        host='localhost',
        database='newflask',
        port=3306,
        charset="utf8",
    )
    cursor = db.cursor()
    return db, cursor


def create_table(cursor, sql):
    try:
        cursor.execute(sql)
    except Exception as e:
        print(e)

