from spider.Day13.MyAgentPool.models import Proxy
import requests
from queue import Queue
from threading import Thread
import time
ipPort_que=Queue(1000)



class Prosuctor(Thread):
    def __init__(self,que,*args,**kwargs):
        super(Prosuctor,self).__init__(*args,**kwargs)
        self.que=que
        self.proxy={"http":""}
    def run(self):
        while True:
            for _ in range(200):
                proxy={}
                proxy_dict=Proxy.get_random()
                proxy['http']=proxy_dict['address']
                self.que.put(proxy)
            time.sleep(5)

class Customer(Thread):
    def __init__(self,que,*args,**kwargs):
        super(Customer,self).__init__(*args,**kwargs)
        self.que=que
        self.url = 'http://httpbin.org/ip'
    def run(self):
        while True:
            dict=self.que.get()
            print(dict)
            self.test_port(dict)
            time.sleep(1)
    def test_port(self,proxy):
        url = 'http://httpbin.org/ip'
        try:
            print("测试" + proxy['http'])
            json = requests.get(url, proxies=proxy,timeout=5).content.decode("utf-8")
            if (proxy['http'].split(':')[0] not in json):
                Proxy.objects.filter(address=proxy['http']).delete()
            else:
                print("测试成功:"+proxy['http'])
        except Exception as e:
            print(e)
            Proxy.objects.filter(address=proxy['http']).delete()
            print("已删除" + proxy['http'])





pro=Prosuctor(ipPort_que)
pro.start()

for _ in range(100):
    t=Customer(ipPort_que)
    t.start()


