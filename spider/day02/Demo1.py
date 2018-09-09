# encoding:utf-8

import requests

params={
    'wd':'中国'
}
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}
resp=requests.get("http://www.baidu.com/s",params=params,headers=headers)

#print(resp.content.decode('utf-8'))

print(resp.url)


with open("1.html",'wb') as file:
    file.write(resp.content)
