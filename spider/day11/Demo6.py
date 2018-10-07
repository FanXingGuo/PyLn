# -*- coding: utf-8 -*-
import asyncio
import aiohttp
from pyquery import PyQuery as pq

urls = ["http://www.mzitu.com/page/{}/".format(i) for i in range(1, 157)]

# 限制并发数为5个
semaphore = asyncio.Semaphore(5)

f = open("img_url.txt", "w")

async def get_html(url):
    ck = """Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1507966069,1509850072,1509851337,1509851651; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1509851653"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Referer": url,
        "Cookie": ck,
        "Host": "www.mzitu.com"
    }
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as html:
                # print(resp.status)
                response = await html.text(encoding="utf-8")
                # print(response)
                return response

async def parse(url):
    html = await get_html(url)
    doc = pq(html)
    img_urls = doc(".postlist ul li a img").items()
    for img_url in img_urls:
        url = img_url.attr("data-original")
        f.write(url + '\n')


loop = asyncio.get_event_loop()
tasks = [parse(url) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

f.close()