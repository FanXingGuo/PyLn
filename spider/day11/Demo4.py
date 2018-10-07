import aiohttp
import time
import asyncio
import requests

URL = 'https://www.baidu.com'

# def normal():
#     for i in range(10):
#         r = requests.get(URL)
#         url = r.url
#         print(url)
#
# t1 = time.time()
# normal()
# print("Normal total time:", time.time()-t1)
# Normal total time: 1.7251458168029785



async def job(session):
    response = await session.get(URL)       # 等待并切换
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session)) for _ in range(100)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)
# Async total time: 0.3639068603515625 10pages
