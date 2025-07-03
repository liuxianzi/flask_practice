# -*- coding: utf-8 -*-
"""
 @Time           2025/7/3 15:59
 @File           14.flask中用到的上下文管理.py
 @Description    
 @Author         
"""
import contextvars

# 创建一个上下文变量 name是 ctx,默认值是89
ctx = contextvars.ContextVar('ctx', default=89)

# 获取ctx的值
print(ctx.get())  # 未设置token ，则返回默认值
# 通过ctx.set() 设置ctx的值
token = ctx.set(20)
print(ctx.get())
# token.var用来指向创建token的ContextVar
print(token.var)
# token.old_value用来保存token之前的值，如果之前未分配过值，则填充token.MISSING
print(token.old_value)
token = ctx.set(100)
token = ctx.set(40)
print(ctx.get())
print(token.old_value)
print('-----------------------------------------------------')
# 通过ctx.reset()重置ctx的值，恢复到设置token操作之前的值
ctx.reset(token)
print(ctx.get())
print(token.old_value)
print(token)

# ctx.reset(token)  # 报错：可以简单理解为： token中只保留 两个值，一个set之前的，一个set后的。
