import asyncio
import aiohttp

semaphore = asyncio.Semaphore(5)

async def run(url):
    headers = {

            "Connection": "keep-alive",
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",

        }


    print("start spider ",url)
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,headers=headers) as resp:
                print(resp.url)
url_list =['https://www.thepaper.cn/newsDetail_forward_{}'.format(i) for i in range(2505000,2505800)]
tasks = [asyncio.ensure_future(run(url)) for url in url_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))