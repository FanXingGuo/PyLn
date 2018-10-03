from spider.day09 import ppcont
from spider.day09 import saveNews
from spider.day09 import pengpaiP2
from queue import Queue
import time
import threading

#save=saveNews.saveNews()


class getNews(threading.Thread):
    def __init__(self,queue,save,*args,**kwargs):
        super(getNews,self).__init__(*args,**kwargs)
        self.news_queue=queue
        self.save=save
    def run(self):
        if int(self.name)>8:
            while not self.news_queue.empty():
                self.saveNew()
        else:
            while True:
                self.saveNew()
    def saveNew(self):
        dict = ppcont.NewsContent(self.news_queue.get()).get_news()
        if dict != None:
            self.save.insert(dict)
# class makeUrl(threading.Thread):
#     def __init__(self,queue,*args,**kwargs):
#         super(makeUrl,self).__init__(*args,**kwargs)
#         self.news_queue=queue
#     def run(self):
#         pengpaiP2.mangerUrl(self.news_queue).go1()
# class checkUrl(threading.Thread):
#     def __init__(self,queue,*args,**kwargs):
#         super(checkUrl,self).__init__(*args,**kwargs)
#         self.new_queue=queue
#     def run(self):
#         pengpaiP2.mangerUrl(self.news_queue).go2()




if __name__=="__main__":
    news_queue=Queue(1000)
    save=saveNews.saveNews()
    print("数据库连接成功!")
    for i in range(8,32):
        t1=getNews(news_queue,save,name=i)
        t1.start()
    m1=pengpaiP2.mangerUrl(news_queue)
    m2=pengpaiP2.mangerUrl(news_queue)
    id=m1.getLastId()
    m2.maxNum=id
    go2=threading.Thread(target=m2.go2)
    go1=threading.Thread(target=m1.go1)
    go2.start()
    go1.start()











