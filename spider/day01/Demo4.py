from urllib import request,parse

url='http://221.232.159.27/tjkbcx.aspx?xh=2016040121081&xm=%B7%B6%D0%CB%B9%FA&gnmkdm=N123101'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=hoaszkmh4gmq3r55v11f3trj',
    'Referer':'http://221.232.159.27/xs_main.aspx?xh=2016040121081'
}


req=request.Request(url,headers=headers,method='POST')
resp=request.urlopen(req)

#print(resp.read())

with open("1.html",'wb') as file:
    file.write(resp.read())