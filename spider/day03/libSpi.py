# encoding:utf-8

from lxml import etree
from urllib import request
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',

}
url='http://lib.wdu.edu.cn/tsgdt/tz/index.shtml'

def getPageUrl(html):

    htmlEle=etree.HTML(html)
    list=htmlEle.xpath("//div[@class='wbz_title']/a/@href")
    title=htmlEle.xpath("//div[@class='wbz_title']/a/text()")
    contList=[]
    # for i,j in list,title:
    #     contList.append([i,j])
    # return contList
    # print(len(list))
    # print(len(title))

def makeAllUrl():
    urlList=["http://lib.wdu.edu.cn/tsgdt/tz/index.shtml"]
    url = 'http://lib.wdu.edu.cn/tsgdt/tz'
    for i in range(2,15):
        urlList.append("http://lib.wdu.edu.cn/tsgdt/tz/index_"+i+".shtml")
    return urlList
def downHtml(url,name):
    request.urlretrieve(url,name)



resp=requests.get("http://lib.wdu.edu.cn/tsgdt/tz/",headers=headers)
#request.urlretrieve(url,"temp.html")

print(resp.content.decode('utf-8'))

