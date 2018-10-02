import requests
from lxml import etree
from queue import Queue
import re
from queue import Queue



class pengpaiP1():
    #cont_queue 用于保存新闻目录地址 :url
    #news_queue 用于保存新闻标题和链接:(title,url)
    def __init__(self,cont_queue,news_queue,url):
        self.headers={
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
        self.cont_queue=cont_queue
        self.news_queue=news_queue
        self.index='https://www.thepaper.cn/'
        self.url=url
        self.pageidx=2
        self.stopUrl=""

    def getTitleAndUrl(self,html,stopUrl):
        try:
            htmlEle = etree.HTML(html)
            urls = htmlEle.xpath('//a[@class="tiptitleImg"]/@href')
            titles = htmlEle.xpath('//a[@class="tiptitleImg"]/img/@alt')
            self.stopUrl=urls[0]
            for index, item in enumerate(urls):
                if item==stopUrl:
                    return False
                url = self.index + item
                self.news_queue.put((titles[index], url))
            return True
        except:
            print("html代码有误")
            print(html)

    def getlastTime(self,html):
        p = re.compile('lastTime="([0-9]+)"')
        result = p.findall(html)
        if len(result) >= 1:
            return result[0]
        else:
            return None
    def getreqUrl(self,html):
        p1 = re.compile('return ("load.+lastTime;)')
        cont = p1.findall(html)
        cont = cont[0:len(cont) - 1]
        return cont
    def Go1(self,stopUrl=None):
        html = requests.get(self.url, headers=self.headers).content.decode("utf-8")
        cont=self.getreqUrl(html)
        link_list = "".join(cont).split('"')
        link_list[0] = self.index
        lastTime = self.getlastTime(html)
        self.getTitleAndUrl(html,stopUrl)
        # print("".join(link_list))

        while lastTime != None:
            # 制造请求链接
            link_list[2] = str(self.pageidx)
            link_list[4] = lastTime
            link = "".join(link_list)
            print(link)
            # 请求
            getHtml = requests.get(link, headers=self.headers).content.decode("utf-8")
            flag=self.getTitleAndUrl(getHtml,stopUrl)
            if not flag:
                break
            # 为下一次做铺垫
            self.pageidx += 1
            lastTime = self.getlastTime(getHtml)


if __name__=="__main__":
    cont_queue = Queue(100)
    news_queue = Queue(1000)
    url='https://www.thepaper.cn/'
    p=pengpaiP1(cont_queue,news_queue,url)
    p.Go1()
    # while not p.news_queue.empty():
    #     print(p.news_queue.get())