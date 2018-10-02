import requests
from lxml import etree
from queue import Queue
import re
from spider.day09 import ppcont

headers={
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
cont_queue=Queue(100)
news_urls=Queue(1000)
pageidx=2

index_url='https://www.thepaper.cn/'
html=requests.get(index_url,headers=headers).content.decode("utf-8")

#html->put((title,url))
def getTitleAndUrl(html):
    try:
        htmlEle=etree.HTML(html)
        urls=htmlEle.xpath('//a[@class="tiptitleImg"]/@href')
        titles=htmlEle.xpath('//a[@class="tiptitleImg"]/img/@alt')
        for index,item in enumerate(urls):
            url=index_url+item
            news_urls.put((titles[index],url))
    except:
        print("html代码有误")
        print(type(html))

#next_time
def getlastTime(html):
    p=re.compile('lastTime="([0-9]+)"')
    result=p.findall(html)
    if len(result)>=1:
        return result[0]
    else:
        return None

#配置 请求链接
p1=re.compile('return ("load.+lastTime;)')
cont=p1.findall(html)
#去除重叠内容
cont=cont[0:len(cont)-1]
link_list="".join(cont).split('"')
link_list[0]=index_url


lastTime=getlastTime(html)

print("".join(link_list))

while lastTime!=None:
    #制造请求链接
    link_list[2] = str(pageidx)
    link_list[4] = lastTime
    link="".join(link_list)
    #请求
    getHtml=requests.get(link,headers=headers).content.decode("utf-8")
    getTitleAndUrl(getHtml)
    print(link)
    #为下一次做铺垫
    pageidx+=1
    lastTime=getlastTime(getHtml)
print("=== ==="*30)

# print(news_urls.qsize())

#遍历队列
while not news_urls.empty():
    print(news_urls.get())











