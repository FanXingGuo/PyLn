# coding=gbk
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
import threading
import requests
from queue import Queue
import pymongo
import time
from lxml import etree
import re





myclient=pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["NewsCont"]
mycol = mydb["pengpai1"]
urls_que=Queue(1000)
urls = ['http://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2504000, 2505000)]

urls_half = ['http://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2504000, 2505000)]

for i in range(1000):
    urls_que.put(urls[i])
headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }


def get_news(url,html):
            cont = {"id": ""}
            htmlEle = etree.HTML(html)

            # 如果是文字新闻
            if len(htmlEle.xpath('//div[@class="news_txt"]')) > 0:
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
                about = " ".join(news_about).replace("\n", "").replace("\t", "").replace(" ", "")
                text = []
                info_conut = 0
                img_count = -1
                nn_flag = False
                for index, item in enumerate(news_txt):
                    if (str(item).startswith("http://image.thepaper.cn")):
                        img_count += 1
                        if img_count <= len(news_imgInfo) - 1 and news_txt[index + 1] == news_imgInfo[info_conut]:
                            text.append([item, news_imgInfo[info_conut].replace("'", '‘').replace('"', '‘')])
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
                        text.append(item.replace("'", '‘').replace('"', '‘'))
                # print(text)
                editor = "".join(news_editor)
                keywords = "".join(news_keywords)
                if ">>" in keywords:
                    keywords = keywords.split(">>")[1]
                else:
                    keywords = ""

                if len(new_video) > 0:
                    p = re.compile("http://cloudvideo.+mp4")
                    link = p.findall(html)
                    video_info = "".join(new_video).replace("\n", "").replace("\t", "")
                    text.insert(0, [link[0], video_info])

                cont["title"] = title.replace("'", '‘').replace('"', '‘')
                cont["path"] = path
                cont["about"] = about
                cont["text"] = text
                cont["editor"] = editor
                cont["keywords"] = keywords
                cont['id'] = str(url).split("_")[-1].replace("\n", "")



            # 如果是视频新闻
            elif len(htmlEle.xpath('//div[@class="video_main pad60 nav_container"]')) > 0:

                title = htmlEle.xpath('//div[@class="video_txt_t"]/h2/text()')[0]
                video_Url = htmlEle.xpath('//source[@type="video/mp4"]/@src')[0]
                video_info = htmlEle.xpath('//div[@class="video_txt_l"]/p/text()')[0].replace(" ", "")
                text = [video_Url, video_info]
                about = htmlEle.xpath('//div[@class="t_source_1"]//text()')[0].replace(" ", "")
                path = '首页-视频'
                keywords = ""
                editor = htmlEle.xpath('//div[@class="video_info_second"]/span[1]/text()')[0]

                cont["title"] = title.replace("'", '‘').replace('"', '‘')
                cont["path"] = path
                cont["about"] = about
                cont["text"] = text
                cont["editor"] = editor
                cont["keywords"] = keywords
                cont['id'] = str(url).split("_")[-1].replace("\n", "")


            myID = str(url).split("_")[-1].replace("\n", "")
            return (cont, myID)

def get_html(url):
    global headers
    try:
        html=requests.get(url,headers=headers).content.decode("utf-8")
        if len(html)>100:
            return html
        else:
            return None
    except Exception as e:
        print("--- --- "*10)
        print(e)
        print(url)
        print("--- --- " * 10)
        return None
def main(url):
    global mycol
    html=get_html(url)
    if html != None:
        # print(len(html))
        dict=get_news(url,html)[0]
        if dict['title']!=None:
            print(dict['id'])
            mycol.insert_one(dict)
    else:
        return None


# == == == == == == == == == == == == == == == == == == == == == ==
# 2多进程 乘以 50多线程 尝试
#
def thd(que,name):

    urlTen=['http://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2504000, 2504010)]
    for url in urlTen:
        main(url)

def thd50(name):
    global urls_que
    for i in range(50):
        t=threading.Thread(target=thd,args=(urls_que,name))
        t.start()








# start=time.time()
# with ThreadPoolExecutor(max_workers=100) as executor:
#         executor.map(main,urls)
# print("# 100 Threads costs {}".format(time.time()-start))


start=time.time()
with ProcessPoolExecutor(max_workers=2) as pt:
    pt.map(main,urls)

print("# 100P costs {}".format(time.time()-start))

# 100 Threads costs 22.24502921104431
# 100 Threads costs 13.429037809371948
# 100 Threads costs 12.240097045898438
# 100 Threads costs 11.542321920394897
# 100 Threads costs 12.889510154724121
# 100 Threads costs 11.882719993591309
# 100 Threads costs 12.867509841918945
# 100 Threads costs 11.663952827453613
# 100 Threads costs 12.480878114700317
# 100 Threads costs 12.220237016677856

#多进程 没有存入 mongoDB

# 100P costs 13.524444103240967
# 100P costs 12.427114009857178
# 100P costs 16.219638109207153
# 100P costs 12.69909381866455
# 100P costs 12.474831104278564
# 100P costs 12.652209997177124





