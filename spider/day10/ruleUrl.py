import requests
from queue import Queue
from lxml import etree
import time
#下载一个时间段的新闻 定期检查新闻更新, 结果存于队列之中

news_url=Queue(1000)
news_tmp=Queue(100)

class mangerUrl():
    def __init__(self,newsQueue=None,tmpQueue=None):
        self.newsQueue=newsQueue
        self.tmpQueue=tmpQueue
        self.headers=headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
        self.url='https://www.thepaper.cn/load_chosen.jsp'
        self.prefix='https://www.thepaper.cn/newsDetail_forward_'
        self.id=self.getLastId()

    def checkNews(self):
        #时间轴更新
        while True:
            newID=self.getLastId()
            new_id=int(newID)
            old_id=int(self.id)
            if new_id>old_id:
                print("发现新的新闻%d篇"%(new_id-old_id))
                self.putAndlog('checkedLog.txt',old_id,new_id,"发现新新闻")
                self.id=newID
            else:
                print("%s 未发现新的新闻,id=%s"%(time.asctime(),self.id))
            time.sleep(3)

    def scanNews(self):
        pass


    def downNews(self,end_id=2503328):
        self.putAndlog("downNews.txt",end_id,int(self.id),"首次下载")

    def putAndlog(self,filename,start,end,event):
        file = open(filename, "a+", encoding="utf-8")
        file.write(time.asctime() + ":" + str(event+"写入%d篇" % (end - start)) + '\n')
        for i in range(start+1, end + 1):
            newsUrl = self.prefix + str(i)
            self.newsQueue.put(newsUrl+'\n')
            file.write(newsUrl + ' wrote\n')
        file.write(str("-- -- " * 10)+'\n')
        file.close()



    def getLastId(self):

        htmlEle=etree.HTML(html)
        id=htmlEle.xpath('//div[@class="news_li"][1]/@id')[0].split("cont")[1]
        return id


if __name__=="__main__":
    mangerUrl(news_url,news_tmp).checkNews()




