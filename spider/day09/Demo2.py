import time
import threading
import random

Money=1000
gLock=threading.Lock()
gTimes=0

class Producter(threading.Thread):
    def run(self):
        global  Money
        global gTimes
        while True:
            gLock.acquire()
            if gTimes>10:
                gLock.release()
                break
            m=random.randint(100,1000)
            Money = Money + m
            print("%s生产了%d,剩下%d"%(threading.current_thread().name,m,Money))
            gTimes+=1
            gLock.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self):
        global Money
        while True:
            gLock.acquire()
            m=random.randint(100,1000)
            if m<=Money:
                Money=Money-m
                print("%s消费者消费了%d,还剩%d"%(threading.current_thread().name,m,Money))
            else:
                gLock.release()
                break
                print("%s消费者欲打算消费%d,但是还剩%d"%(threading.current_thread().name,m,Money))
            gLock.release()
            time.sleep(1)


for i in range(3):
    t=Consumer(name="C"+str(i))
    t.start()

for i in range(5):
    t=Producter(name="P"+str(i))
    t.start()





