import asyncio
import aiohttp
from lxml import etree
import time
import multiprocessing as mp
import socket

semaphore = asyncio.Semaphore(200)

headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }

urls=['http://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2504000,2505000)]


# async def getHtml(url):
#     headers = {
#
#         "Connection": "keep-alive",
#         "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
#         "X-Requested-With": "XMLHttpRequest",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.8",
#
#     }
#     async with semaphore:
#         async with aiohttp.ClientSession as session:
#             async with session.get(url,headers=headers) as resp:
#                 html=await resp.text(encoding="utf-8")
#             return html

t1=time.time()

async def get_html(url,session):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
    }
    try:
        async with session.get(url, headers=headers) as html:
            # print(resp.status)
            response = await html.text(encoding="utf-8")
            # asyncio.sleep(0.1)
            # print(response)
            return response
    except Exception as e:
        print("-- -- "*20)
        print(e)
        print(url)
        print("-- -- " * 20)

async def parse(url):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            html=await get_html(url,session)
            print(url)
    # if len(html)>100:
    #     htmlEle=etree.HTML(html)
    #     title=htmlEle.xpath("//title/text()")
    #     print(title)


def pro():
    loop = asyncio.get_event_loop()
    task=[parse(url) for url in urls]
    loop.run_until_complete(asyncio.wait(task))

t1=time.time()
# pro()
p1=mp.Process(target=pro)
p2=mp.Process(target=pro)
# p1.start()
p2.start()
# p1.join()
p2.join()
print("Cost {}".format(time.time()-t1))

#Cost 4.723982095718384