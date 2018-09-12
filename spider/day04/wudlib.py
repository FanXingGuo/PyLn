# encoding:utf-8

from lxml import etree
from urllib import request
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',

}
url='http://lib.wdu.edu.cn/tsgdt/tz/index.shtml'
pre_url='http://lib.wdu.edu.cn/tsgdt/tz/'


#对于每一页,获取通知链接 url-->news_url
def getPageUrl(url):
    html=requests.get(url,headers=headers).content.decode('gb2312')
    #print(html)
    htmlEle=etree.HTML(html)


    lists=htmlEle.xpath("//div[@class='wbz_title']/a/@href")

    # //div[@class='wbz_title']/a/text() 下面增加对 色彩处理代码的应变
    title=htmlEle.xpath("//div[@class='wbz_title']//text()")


    contList=[]

    for index,url in enumerate(lists):
        if url.startswith("http"):
            contList.append([title[index] + '.html',url])
            continue
        if '/' in title[index]:
            title[index]=title[index].replace("/", "-")
        contList.append([title[index]+'.html',pre_url+url[2:]])

    #print(contList)
    return contList

#产生所以 通知板块所有页面链接
def makeAllUrl():
    # urlList=["http://lib.wdu.edu.cn/tsgdt/tz/index.shtml"]
    # url = 'http://lib.wdu.edu.cn/tsgdt/tz'
    # for i in range(2,15):
    #     urlList.append("http://lib.wdu.edu.cn/tsgdt/tz/index_"+i+".shtml")


    #way2
    urlLists=[]
    url1="http://lib.wdu.edu.cn/tsgdt/tz/index_{}.shtml"

    for i in range(1,14):
        urlLists.append(url1.format(i))
    urlLists.insert(0,'http://lib.wdu.edu.cn/tsgdt/tz/index.shtml')

    #print(urlLists)


    return urlLists


def downHtml(url,name):
    request.urlretrieve(url,name)




#
# getPageUrl(html)


if __name__ == '__main__':
    urls=makeAllUrl()
    cout=0;
    for url in urls:
        items=getPageUrl(url)
        for item in items:
            name=item[0]
            link=item[1]
            print(name+"  "+link)
            cout=cout+1
            downHtml(link,name)
            print(cout)








