#encoding=gbk
import asyncio
import aiohttp
from lxml import etree
import pymongo
import re

myclient=pymongo.MongoClient("mongodb://localhost:27107")
mydb=myclient["NewsCont"]
mycol=mydb["pengpai1"]

semaphore=asyncio.Semaphore(100)

urls=['http://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2504000,2505000)]

async def getHtml(url,session):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    }
    try:
        async with session.get(url,headers=headers) as resp:
            html=await resp.text(encoding="utf-8")
            return html
    except Exception as e:
        print("-- -- " * 20)
        print(e)
        print(url)
        print("-- -- " * 20)
        return None
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

def insertMongo(dict):
    global mycol
    mycol.insert(dict)

async def parse(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            html=await getHtml(url,session)
            if html !=None and len(html)>100:
                dict=get_news(url,html)[0]
                # insertMongo(dict)
                print(dict[0])


loop=asyncio.get_event_loop()
tasks=[parse(url) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))





