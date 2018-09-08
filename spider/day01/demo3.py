from urllib import request

url='http://httpbin.org/ip'
# resp=request.urlopen(url)
# print(resp.read())

#代理
hander=request.ProxyHandler({"http":"115.223.203.197:9000"})
opener=request.build_opener(hander)
resp=opener.open(url)

print(resp.read())