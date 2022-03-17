#!/usr/bin/env/python
# _*_ encoding: utf-8 _*_
'''
@File		:	CH2_字符串.py
@Time		:	2022/03/17 13:05
@Author		:	Wekkin
@Version	:	1.0
@Contact	:	dengwq1997@163.com
@License	:	(C)Copyright 2022-2023
@Desc		:	None
'''

# add import lib

from email import message


name = "ada lovelace"
print(name.title())
# title()表示首字母大写

print(name.upper())
# upper()全字母大写

print(name.lower())
# lower()全字母小写

"""CH2_字符串拼接"""
first_name = "ada"
last_name = "lovelace"
full_name =first_name +" "+ last_name
message = "hello, " +full_name.title() +"!"
print(message)
# 使用+加号来合并字符串，这种方法叫拼接，通过拼接可以让储存在变量的信息创建完整的消息

"""使用制表符或者换行符添加空白"""
print("Python")
print("\tPython")
# \t 制表符 空格

print("\nPython\nC\nJava")
# \n 换行

print("\n\tPython\n\tC\n\tJava")
# \n\t 换行再空格

"""删除空格"""
favorite_language = 'Python   '
print(favorite_language)
print(favorite_language.rstrip())
# rstrip()暂时性删除尾部空格
# lstrip()删除开头空格
# strip()删除两端空格 

