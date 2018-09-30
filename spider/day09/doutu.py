import requests
from urllib import request
import threading
from queue import Queue
from lxml import etree
import os
import re



#形成前100页URL


class Productor(threading.Thread):
    headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }

    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Productor,self).__init__(*args,**kwargs)
        self.page_queue=page_queue
        self.img_queue=img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            html=requests.get(self.page_queue.get(),headers=self.headers).content.decode("utf-8")
            imgs=etree.HTML(html).xpath("//div[@class='page-content text-center']//a/img")
            for img in imgs:
                img_url=img.get("data-original")
                img_title=img.get("alt")
                if img_url!=None:
                    suffix="."+img_url.split(".")[-1]
                    filename=img_title+suffix
                    print((filename,img_url))
                    self.img_queue.put((filename,img_url))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.img_queue=img_queue
        self.page_queue=page_queue
    def run(self):
        while True:
            if self.page_queue.empty() and self.img_queue.empty():
                break
            img_url=self.img_queue.get()
            request.urlretrieve(img_url[1],"images/"+img_url[0])











#图片地址 //div[@class='page-content text-center']//a/img/@src
#图片描述 //div[@class='page-content text-center']//a/img/@alt

if __name__=="__main__":
    page_queue = Queue(100)
    img_queue = Queue(1000)
    headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
    for i in range(1, 101):
        url = 'http://www.doutula.com/photo/list/?page=%d' % i
        page_queue.put(url)

    for i in range(5):
        t1=Productor(page_queue,img_queue)
        t1.start()

        c1=Consumer(page_queue,img_queue)
        c1.start()


