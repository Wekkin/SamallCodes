# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:19:16 2022
@author: Wekkin
"""

import requests
import base64
import datetime
import os
import keyboard
from PIL import ImageGrab

'''
#需要用Snipaste快捷贴图到剪贴板，触发事件
keyboard.wait(hotkey = "f1")
keyword.wait(hotkey = "ctlr+c")
time.sleep(0.1)

image = ImageGrab.grabclipboard()
image.save("1.png")
'''


#通用文字识别百度API

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
#删除图片，测试删除"2.png"
os.remove('2.png')
path_lists = ['效果图','客户要求','其他测试图']
for path_list in path_lists:
    path = '/home/Test/'+(keyword)+'/'+(path_list)
    if not os.path.exists(path):
        os.makedirs(path)
print("文件夹以已建立")



