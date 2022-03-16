# -*- coding: utf-8 -*-

import datetime
import base64
import requests
import os


# 获取access_token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
appid = "25527290"
client_id = "0IBW39ejOiB5W5xstmaZF8q1"
client_secret = "6sU8Gjt5Z4kmFqGBTHj0G20Fg6ggFii8"
token_url = "https://aip.baidubce.com/oauth/2.0/token"
host = f"{token_url}?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"
response = requests.get(host)
access_token = response.json().get("access_token")
print("新Token是: " + access_token)
# 调用通用文字识别高精度版接口
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
request_url = f"{request_url}?access_token={access_token}"


# 二进制方式打开图片文件
# 参数image：图像base64编码
# 添加图片的绝对路径
f = open('C:\\Users\\DWQ\\Desktop\\1.png', 'rb')
img = base64.b64encode(f.read())
params = {"image": img}
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, headers=headers, data=params)
if response:
    #print (response.json())
    src = (response.json())

# 关键字
timetoday = datetime.datetime.now()
datetoday = timetoday.strftime("%Y%m%d")
keyword = ((datetoday)+("-") +
           (src['words_result'][3]['words'])+("-") +
           (src['words_result'][1]['words'])+("-") +
           (src['words_result'][2]['words'])+("-") +
           (src['words_result'][4]['words'])+("-") +
           (src['words_result'][0]['words']))
#print (keyword)

path_lists = ['测试效果、配置表', '客户要求、联络函']
for path_list in path_lists:
    # win11，下最终文件生成路径
    path = 'C:\\Users\\DWQ\\Desktop\\'+(keyword)+'\\'+(path_list)

    # liunx,最终文件生成路径
    # path = '/home/Test/'+(keyword)+'/'+(path_list)

    if not os.path.exists(path):
        os.makedirs(path)

# 将PPT模板放入生成的文件夹里;模板.PPT -->path:并且根据当天文件重新命名.
print("文件夹以已建立")
