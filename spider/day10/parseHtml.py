#encoding:utf-8
import requests
from lxml import etree
import re


class NewsContent:
    def __init__(self,url,html):
        self.url=url
        self.html=html
        self.log=""
    def get_news(self):
        cont = {"id": ""}
        if self.html==None:
            myID = str(self.url).split("_")[-1].replace("\n","")
            self.save_log(self.log)
            return (None, myID)

        htmlEle = etree.HTML(self.html)
        #如果网页加载失败
        if htmlEle == None:
            self.log=self.log+"htmlEle is None"
            cont=None
        #如果是文字新闻
        elif len(htmlEle.xpath('//div[@class="news_txt"]')) > 0:
            news_title = htmlEle.xpath("//div[@class='newscontent']/h1/text()")
            news_path = htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_path"]/a//text()')
            news_about = htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_about"]/p//text()')
            new_video = htmlEle.xpath('//div[@class="news_video_name"]/text()')
            news_txt = htmlEle.xpath('//div[@class="news_txt"]//text()|//div[@class="news_txt"]/div/img/@src')
            news_imgInfo = htmlEle.xpath('//div[@class="news_txt"]/span/text()')
            news_editor = htmlEle.xpath("//div[@class='newscontent']/div[@class='news_editor']/text()")
            news_keywords = htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_keyword"]/text()')



            title = "".join(news_title).replace("\n", "").replace("\t", "")
            path = "-".join(news_path)
            about = " ".join(news_about).replace("\n", "").replace("\t", "").replace(" ","")
            text = []
            info_conut = 0
            img_count = -1
            nn_flag = False
            for index, item in enumerate(news_txt):
                if (str(item).startswith("http://image.thepaper.cn")):
                    img_count += 1
                    if img_count <= len(news_imgInfo) - 1 and news_txt[index + 1] == news_imgInfo[info_conut]:
                        text.append([item, news_imgInfo[info_conut].replace("'",'‘').replace('"','‘')])
                        info_conut += 1
                        nn_flag = True
                    else:
                        # 处理图片描述长度不足问题
                        text.append([item, ""])
                        continue
                else:
                    if (nn_flag):
                        nn_flag = False
                        continue
                    text.append(item.replace("'",'‘').replace('"','‘'))
            # print(text)
            editor = "".join(news_editor)
            keywords = "".join(news_keywords)
            if ">>" in keywords:
                keywords=keywords.split(">>")[1]
            else:
                keywords=""

            if len(new_video) > 0:
                p = re.compile("http://cloudvideo.+mp4")
                link = p.findall(self.html)
                video_info="".join(new_video).replace("\n", "").replace("\t", "")
                text.insert(0,[link[0],video_info])



            cont["title"] = title.replace("'",'‘').replace('"','‘')
            cont["path"] = path
            cont["about"] = about
            cont["text"] = text
            cont["editor"] = editor
            cont["keywords"] = keywords
            cont['id']=str(self.url).split("_")[-1].replace("\n","")



        #如果是视频新闻
        elif len(htmlEle.xpath('//div[@class="video_main pad60 nav_container"]'))>0:

            title=htmlEle.xpath('//div[@class="video_txt_t"]/h2/text()')[0]
            video_Url=htmlEle.xpath('//source[@type="video/mp4"]/@src')[0]
            video_info=htmlEle.xpath('//div[@class="video_txt_l"]/p/text()')[0].replace(" ","")
            text=[video_Url,video_info]
            about=htmlEle.xpath('//div[@class="t_source_1"]//text()')[0].replace(" ","")
            path='首页-视频'
            keywords=""
            editor=htmlEle.xpath('//div[@class="video_info_second"]/span[1]/text()')[0]

            cont["title"] = title.replace("'", '‘').replace('"', '‘')
            cont["path"] = path
            cont["about"] = about
            cont["text"] = text
            cont["editor"] = editor
            cont["keywords"] = keywords
            cont['id'] = str(self.url).split("_")[-1].replace("\n","")
        else:
            self.log=self.log+"can not parse"

        myID=str(self.url).split("_")[-1].replace("\n","")
        self.save_log(self.log)
        return (cont,myID)



    def save_log(self,rowText):

        with open("parseHtml.txt","a+",encoding="utf-8") as file:
            file.write(str(self.url).split("_")[-1].replace("\n","")+"  "+rowText+'\n')



    def has_news(self):
        return len(etree.HTML(self.html).xpath('//div[@class="news_txt"]')) > 0

def makeSql(dict):
    sql = 'insert into pp_News(title,path,about,content,editor,keywards) VALUES ("%s","%s","%s","%s","%s","%s")' % (
        dict['title'], dict['path'], dict['about'], dict['text'], dict['editor'], dict['keywords'])
    print(sql)

if __name__=='__main__':
    headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
    url = "https://www.thepaper.cn/newsDetail_forward_2502532"
    html=requests.get(url,headers=headers).content.decode("utf-8")
    news=NewsContent(url,html)
    d=news.get_news()
    print(d[1])




# cont={}
# html=requests.get(url,headers=headers).content.decode("utf-8")
# #print(html)
# htmlEle=etree.HTML(html)
# if len(htmlEle.xpath('//div[@class="news_txt"]'))>0:
#     news_title=htmlEle.xpath("//div[@class='newscontent']/h1/text()")
#     news_path=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_path"]/a//text()')
#     news_about=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_about"]/p//text()')
#     new_video=htmlEle.xpath('//div[@class="news_video_name"]/text()')
#     news_txt=htmlEle.xpath('//div[@class="news_txt"]//text()|//div[@class="news_txt"]/div/img/@src')
#     news_imgInfo=htmlEle.xpath('//div[@class="news_txt"]/span/text()')
#     news_editor=htmlEle.xpath("//div[@class='newscontent']/div[@class='news_editor']/text()")
#     news_keywords=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_keyword"]/text()')
#
#     if len(new_video)>0:
#         print(new_video)
#         print("-----"*20)
#         p=re.compile("http://cloudvideo.+mp4")
#         link=p.findall(html)
#         #print(re.match("(http://cloudvideo.+mp4)",html))
#         print(link)
#         print("-----" * 20)
#
#     title="".join(news_title).replace("\n","").replace("\t","")
#     path="-".join(news_path)
#     about=" ".join(news_about).replace("\n","").replace("\t","")
#     text=[]
#     info_conut=0
#     img_count=-1
#     nn_flag=False
#     for index,item in enumerate(news_txt):
#         if(str(item).startswith("http://image.thepaper.cn")):
#             img_count+=1
#             if img_count<=len(news_imgInfo)-1 and news_txt[index+1]==news_imgInfo[info_conut] :
#                 text.append([item,news_imgInfo[info_conut]])
#                 info_conut += 1
#                 nn_flag=True
#             else:
#                 #处理图片描述长度不足问题
#                 text.append([item, ""])
#                 continue
#         else:
#             if(nn_flag):
#                 nn_flag=False
#                 continue
#             text.append(item)
#     # print(text)
#     editor="".join(news_editor)
#     keywords="".join(news_keywords).split(">>")[1]
#
#     cont["title"]=title
#     cont["path"]=path
#     cont["about"]=about
#     cont["text"]=text
#     cont["editor"]=editor
#     cont["keywords"]=keywords
#
#
#     print(cont)
#
#
#
#
#     print("=== ===" * 20)
#     print(editor)
#     print(keywords)
#     print("=== ===" * 20)
#
#
#
#
# # print(news_title)
# # print("=== ==="*20)
# # print(news_path)
# # print("=== ==="*20)
# # print(news_about)
# # print("=== ==="*20)
# # for item in news_txt:
# #     print(item)
# #     print("=== ===" * 20)
#
# print("=== ==="*20)
# print(news_editor)
# print("=== ==="*20)
# print(news_keywords)
# print("=== ==="*20)
# # #对于图片信息 获取了两次 一次在txt 一次是专门获取再info 如果图片后面的 和 info的里面的内容有一致的则为图片描述
# print(news_imgInfo)


