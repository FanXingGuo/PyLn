import pymysql
import time
from spider.day10 import parseHtml
import requests



class saveNews():
    def __init__(self):
        self.db = pymysql.connect("ip", "username", "password", "DBname")
        self.cursor = self.db.cursor()
        self.dict=None
        self.id=""
        self.log=""
    def save(self,tup):
        id=tup[1].replace("\n","")
        dict=tup[0]
        # self.commit(dict)
        if dict !=None:
            try:
                self.log=""
                self.commit(dict)
                print(self.sql)
                self.saveLog(id)
            except:
                self.__init__()
                self.log=" first trying Filed"
                try:
                    self.commit(dict)
                except:
                    self.log=" mysql connected,but filed "+"  SQL:"+self.sql
        else:
            self.log=""
            self.log+=" ,dict is None"
        self.saveLog(id)
    def saveLog(self,id):
        timeNow = time.asctime()
        with open("saveNewsLog.txt", "a+", encoding="utf-8") as file:
            file.write(timeNow+' id='+id +self.log+'\n')
        file.close()

    def commit(self,dict):
        #运行用
        self.sql = 'insert into pp_News3(id,title,path,about,content,editor,keywards) VALUES (%s,"%s","%s","%s","%s","%s","%s")' % (
            dict['id'], dict['title'], dict['path'], dict['about'], dict['text'], dict['editor'], dict['keywords'])

        #sql='INSERT INTO test (timeLog) VALUES ("%s")'%(dict)
        self.cursor.execute(self.sql)
        self.db.commit()

if __name__=="__main__":
    s=saveNews()
    url='https://www.thepaper.cn/newsDetail_forward_2500000'
    html=requests.get(url).content.decode("utf-8")
    tup=parseHtml.NewsContent(url,html).get_news()
    s.save(tup)











