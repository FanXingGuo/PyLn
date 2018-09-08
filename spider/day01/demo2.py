from urllib import request,parse

url="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Referer":"https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput="
}

data={
    "first":"true",
    "pn":'1',
    "kc":"python"
}

req=request.Request(url,headers=headers,data=parse.urlencode(data).encode("utf-8"),method='POST')
result=request.urlopen(req)

print(result.read().decode('utf-8'))
