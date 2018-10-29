import requests
from lxml import etree
from spider.Day13.MyAgentPool.models import Proxy
from fake_useragent import UserAgent
import time
from concurrent.futures import ThreadPoolExecutor

url='https://www.kuaidaili.com/free/inha/{}/'
urls=[url.format(i) for i in range(1,1000)]


def getIpList(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
    }
    headers['User-Agent']=UserAgent().random
    if Proxy.objects.filter().count()==0:
        try:
            html = requests.get(headers=headers, url=url, timeout=5).content.decode("utf-8")
        except Exception as e:
            print(e)
            return []
    else:
        dic = Proxy.get_random()
        proxy = {}
        proxy["http"] = dic["address"]
        try:
            html=requests.get(headers=headers,url=url,proxies=proxy,timeout=5).content.decode("utf-8")
        except:
            Proxy.objects.filter(address=proxy['http']).delete()
            return[]
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
while True:
    for item in urls:
        getAndsave(item)
        time.sleep(1)



# import threadpool
# pool=threadpool.ThreadPool(10)
# reqs=threadpool.makeRequests(getAndsave,urls)
# [pool.putRequest(req) for req in reqs]
# pool.wait()

# ex=ThreadPoolExecutor(max_workers=30)
# res_iter=ex.map(getAndsave,urls)






