# -*- coding: utf-8 -*-

#Created on Sat Jan 22 00:19:16 2022

#@author: Wekkin


import requests
import base64
import datetime
import os


'''
截图
'''
#__sizex__, __sizey__ = pag.size()
#pag.alert(text='将图片放在左上角开始截图',title='消息框',button='OK')
#pag.screenshot('1.png',region=(0,0,650,33))


'''
API通用文字识别
'''
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('C:\\Users\\DWQ\\Desktop\\1.png', 'rb')
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

path_lists = ['效果图','客户要求','其他测试图']
for path_list in path_lists:
    
    '''
    win11，下最终文件生成路径
    '''
    path = 'C:\\Users\\DWQ\\Desktop\\'+(keyword)+'\\'+(path_list)
    
    '''
    liunx,z最终文件生成路径
    path = '/home/Test/'+(keyword)+'/'+(path_list)
    '''
    if not os.path.exists(path):
        os.makedirs(path)
print("文件夹以已建立")












