import gevent
from gevent import monkey;monkey.patch_all()
import time
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
from queue import Queue

from lxml import etree



def lenhtml(a):
    headers = {

        "Connection": "keep-alive",
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8",

    }
    url = 'https://www.thepaper.cn/newsDetail_forward_{}'
    s=time.time()
    html=requests.get(url.format(a),headers=headers).content.decode("utf-8")
    #print("{} url open cost{}".format(a,time.time()-s))
    # if len(html)>100:
    #     htmlEle=etree.HTML(html)
    #     title=htmlEle.xpath("//title/text()")
    #     print(title)
    #     return len(html)
    return len(html)

t2=time.time()
Numbers=range(2505000,2505800)
start=time.time()
for num,result in zip(Numbers,map(lenhtml,Numbers)):
    pass
print("顺序执行 cost:{}".format(time.time()-start))

# start=time.time()
# greenlets=[gevent.spawn(lenhtml,a) for a in Numbers]
# gevent.joinall(greenlets)
# print("gvent cost:{}".format(time.time()-start))

# start=time.time()
# with ThreadPoolExecutor(max_workers=10) as executor:
#     for num,result in zip(Numbers,executor.map(lenhtml,Numbers)):
#         #print(str(num)+"  "+str(result))
#         pass
# print("threads cost:{}".format(time.time() - start))

print("ALL {}".format(time.time()-t2))

# gvent cost:7.0102219581604
# threads cost:6.941188812255859
# ALL 13.95156478881836
# Cost 7.774145126342773


# start=time.time()
# url_que=Queue(1000)
# url = 'http://www.wxapp-union.com/portal.php?mod=list&catid=2&page={}'
# for i in Numbers:
#     url_que.put(url.format(i))
#
# class downThd(threading.Thread):
#     def __init__(self,que,*args,**kwargs):
#         super(downThd,self).__init__(*args,**kwargs)
#         self.que=que
#         self.headers=headers = {
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
#     def run(self):
#         while not self.que.empty():
#             url=self.que.get()
#             s = time.time()
#             html = requests.get(url, headers=self.headers).content.decode("utf-8")
#             print("{} url open cost{}".format(len(html), time.time() - s))
#
# for i in range(10):
#     t=downThd(url_que)
#     t.start()





