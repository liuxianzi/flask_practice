# -*- coding: utf-8 -*-
"""
 @Time           2025/6/25 22:20
 @File           d.py
 @Description    
 @Author         
"""
import functools


def decorate(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        return func(*args, **kwargs)
    return wrap


@decorate
def one(a, b):
    return a + b

print(one(2, 3))
# 被装饰器装饰后，one函数会被wrap函数取代，加上@functools.wraps(func) 才会保持原样
print(one.__name__)
