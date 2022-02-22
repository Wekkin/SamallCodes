# encoding:utf-8
import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=0IBW39ejOiB5W5xstmaZF8q1&client_secret=6sU8Gjt5Z4kmFqGBTHj0G20Fg6ggFii8'
response = requests.get(host)
if response:
    print(response.json())
