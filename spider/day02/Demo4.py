import requests

url='http://www.renren.com/PLogin.do'
furl='http://www.renren.com/880151247/profile'
data={
    'email':'office2012.rain@gmail.com',
    'password':'密码'
}

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',

}

session =requests.Session()
session.post(url,data=data,headers=headers)
resp=session.get(furl)

with open("1.html",'wb') as file:
    file.write(resp.content)