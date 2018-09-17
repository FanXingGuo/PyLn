#关于今日头条的 as cp 算法，只是对时间进行了加密，他们的js代码是压缩处理的，正常格式化就可以了

from requests import session
import json
import hashlib
import time
import requests


url = "http://www.toutiao.com/api/pc/feed/"
now = round(time.time())
i = hashlib.md5(str(int(now)).encode('utf-8')).hexdigest().upper()


data = {

    "category":"news_game",
    "utm_source":"toutiao",
    "widen":str(i),
    "max_behot_time":"0",
    "max_behot_time_tmp":"0",
    "tadrequire":"true",
    "as":"479BB4B7254C150",
    "cp":"7E0AC8874BB0985",
}
headers = {

        "Host":"www.toutiao.com",
        "Connection":"keep-alive",
        "Accept":"text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded",
        "Referer":"http://www.toutiao.com/ch/news_hot/",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",

}

result1 = requests.get(url=url,params=data,headers=headers).content.decode('utf-8')
result2 =json.loads(result1)
print(result1)
print("="*30)
print(result2)