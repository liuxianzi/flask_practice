# -*- coding: utf-8 -*-
"""
 @Time           2025/6/28 16:22
 @File           settings.py
 @Description    配置文件
 @Author         
"""

#  其中所有配置变量名必须大写

# 一般写测试环境的配置信息，防止误改正式环境
ENV = 'test'
NAME = '我是测试环境啦'

# 引入本地配置后，ENV，NAME的值就会被覆盖
try:
    from .localsettings import *
except ImportError:
    pass
