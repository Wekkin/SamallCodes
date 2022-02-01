# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 02:19:16 2022

@author: Wekkin
"""
import requests
import base64
import datetime
import os

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('1.png', 'rb')
img = base64.b64encode(f.read())
params = {"image":img}
access_token = '[24.f66c9e347d187be34d59bd5422e4f298.2592000.1645380250.282335-25527290]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    #print (response.json())
    src =(response.json())
timetoday = datetime.datetime.now()
datetoday = timetoday.strftime("%Y%m%d")
keyword = ((datetoday)+("-")+
    (src['words_result'][3]['words'])+("-")+
    (src['words_result'][1]['words'])+("-")+
    (src['words_result'][2]['words'])+("-")+
    (src['words_result'][4]['words'])+("-")+
    (src['words_result'][0]['words']))
#print (keyword)
path_list = ['效果图','客户要求']
path = '/home/Test/'+(keyword)+'/'+(path_list[0])
if not os.path.exists(path):
    os.makedirs(path)
print((keyword)+"文件夹以已建立")