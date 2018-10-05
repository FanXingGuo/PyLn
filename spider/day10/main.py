import threading
import requests
from queue import Queue

from spider.day10 import parseHtml
from spider.day10 import saveNews
from spider.day10 import ruleUrl

gLock=threading.Lock()

#多线程下载网页
class downLoador(threading.Thread):
    def __init__(self,newsUrlQue,newContQue,*args,**kwargs):
        super(downLoador,self).__init__(*args,**kwargs)
        self.newUrlQue=newsUrlQue
        self.newContQue=newContQue
        self.headers=headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
    def run(self):
        while True:
            url=self.newUrlQue.get()
            html=requests.get(url,headers=self.headers).content.decode("utf-8")
            # gLock.acquire()
            # file=open("downLoador.txt","a+",encoding="utf-8")
            # file.write(url+'\n')
            # file.close()
            # gLock.release()
            self.newContQue.put((url,html))


class parseAndsave(threading.Thread):
    def __init__(self, newContQue, *args, **kwargs):
        super(parseAndsave, self).__init__(*args, **kwargs)
        self.newConQue=newContQue
        self.save=saveNews.saveNews()
        self.dict=None
    def run(self):
        while True:
            (url,html)=self.newConQue.get()
            self.dict=parseHtml.NewsContent(url,html).get_news()
            if self.dict[1]!=None:
                self.save.save(self.dict)

if __name__=="__main__":
    newQue=Queue(1000)
    conQue=Queue(1000)
    #配置生产者
    m=ruleUrl.mangerUrl(newQue)
    mThdChe=threading.Thread(target=m.checkNews)
    mThdDon=threading.Thread(target=m.downNews)

    mThdChe.start()
    mThdDon.start()

    #配置消费者
    for i in range(8):
        t=downLoador(newQue,conQue)
        t.start()

    #配置解析器
    pAd=parseAndsave(conQue)
    pAd.start()






