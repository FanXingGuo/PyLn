from queue import Queue
import requests
from lxml import etree
import threading
import time


class mangerUrl():
    def __init__(self,n_queue=None):
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }
        self.url='https://www.thepaper.cn/load_chosen.jsp'
        self.news_queue=n_queue
        self.url_prefix='https://www.thepaper.cn/newsDetail_forward_'
        self.html=requests.get(self.url,headers=self.headers).content.decode("utf-8")
        self.maxNum=2490000
    def go1(self):
        id=self.getLastId()
        # 从考虑新闻时效性问题 获取id 2400000+的新闻 ,2018-09-01 07:28 之后的
        print(id)
        print(self.maxNum)
        for i in range(id,self.maxNum,-1):
            self.putNewsUrl(i)
    def go2(self):
        while True:
            #2499174
            self.html=requests.get(self.url,headers=self.headers).content.decode("utf-8")
            if self.getLastId()>self.maxNum:
                print("发现新的新闻,共计%d篇"%(self.getLastId()-self.maxNum))
                for i in range(self.maxNum,self.getLastId()):
                    print("写入队列id=%07d"%i)
                    self.putNewsUrl(i)
                self.maxNum=self.getLastId()
            else:
                print("最后id为:%s"%str(self.getLastId()))
                print("%s:未发现新的新闻"%time.asctime())
            time.sleep(3)

    def putNewsUrl(self,id):
        news_url = self.url_prefix + str("%07d" % id)
        print(news_url)
        self.news_queue.put(news_url)

    def getLastId(self):
        return int(etree.HTML(self.html).xpath('//div[@class="news_li"][1]/@id')[0].split("cont")[1])


if __name__=="__main__":
    news_queue = Queue(1000)
    mangerurl=mangerUrl(news_queue)
    #mangerurl.maxNum=2498860
    mangerurl.go1()
    while not news_queue.empty():
        print(news_queue.get())











