import threading

VALUE=0

gLock=threading.Lock()

def addValue():
    global VALUE
    for i in range(0,1000000):
        gLock.acquire()
        VALUE=VALUE+1
        gLock.release()
    print(VALUE)



for i in range(0,2):
    t=threading.Thread(target=addValue)
    t.start()