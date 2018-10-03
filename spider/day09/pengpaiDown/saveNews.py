#encoding:utf-8
import pymysql
from spider.day09 import ppcont

class saveNews():
    def __init__(self):
        self.db = pymysql.connect("mysql_ip", "username", "password", "DBname")
        self.cursor = self.db.cursor()

    def insert(self,dict):
        if dict==None:
            return
        try:
            sql='insert into pp_News(title,path,about,content,editor,keywards) VALUES ("%s","%s","%s","%s","%s","%s")'%(
                                dict['title'],dict['path'],dict['about'],dict['text'],dict['editor'],dict['keywords'])
            print(sql)
            # cont["title"] = title
            # cont["path"] = path
            # cont["about"] = about
            # cont["text"] = text
            # cont["editor"] = editor
            # cont["keywords"] = keywords
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            print("内容插入有误")
            print(dict)
    def reConnect(self):
        self.__init__()

    def close(self):
        self.db.close()

if __name__=="__main__":
    url = "https://www.thepaper.cn/newsDetail_forward_2497570"
    news =ppcont.NewsContent(url)
    save=saveNews()
    save.insert(news.get_news())
    save.close()


