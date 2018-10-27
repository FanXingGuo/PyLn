import requests
from lxml import etree
from spider.Day13.MyAgentPool.models import Proxy
from fake_useragent import UserAgent
import time
from concurrent.futures import ThreadPoolExecutor

url='https://www.kuaidaili.com/free/inha/{}/'
urls=[url.format(i) for i in range(3,101)]

headers={
    "User-Agent":'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
}
def getIpList(url):
    headers['User-Agent']=UserAgent().random
    html=requests.get(headers=headers,url=url).content.decode("utf-8")
    time.sleep(3)
    htmlEle=etree.HTML(html)
    ipList=htmlEle.xpath('//td[@data-title="IP"]/text()')
    portList=htmlEle.xpath('//td[@data-title="PORT"]/text()')
    ipPorts=[]
    for index,item in enumerate(ipList):
        ipPorts.append(item+":"+portList[index])
    return ipPorts

def saveIpPorts(ipPort):
    proxy=Proxy(address=ipPort)
    try:
        proxy.save()
    except Exception as e:
        print(e)

def getAndsave(url):
    ipLists=getIpList(url)
    for item in ipLists:
        saveIpPorts(item)
        print(item)

for item in urls:
    getAndsave(item)

# import threadpool
# pool=threadpool.ThreadPool(10)
# reqs=threadpool.makeRequests(getAndsave,urls)
# [pool.putRequest(req) for req in reqs]
# pool.wait()

# ex=ThreadPoolExecutor(max_workers=30)
# res_iter=ex.map(getAndsave,urls)






