# _*_coding: UTF-8 _*_
import urllib2
import re
import os
import threading

def getCon():
    rr=re.compile(r'href="http:\/\/calculus\.yuyumagic424\.net\/\?cat=\d+">.+</a>')
    rcon=re.compile(r'\".+\"')
    rcont=re.compile(r'>.+<')

    resp=urllib2.urlopen("http://calculus.yuyumagic424.net/")
    t=resp.read()
    arr= rr.findall(t)

    con=[]

    for i in arr:
        a=[]
        a.append(rcon.findall(i)[0][1:-1])
        a.append(rcont.findall(i)[0][1:-1])
        con.append(a)
    return con
def getCteLink(link):
    rrCtue=re.compile(r'href="http:\/\/calculus\.yuyumagic424\.net\/\?p=.+>Continue')

    resp=urllib2.urlopen(link)
    t=resp.read()
    arr=rrCtue.findall(t)
    cte=[]
    for i in arr:

        cte.append(i[6:-10])
    return cte
def getPDFandNAME(link):
    rrTitle=re.compile(r'; .+<')
    rrPDF=re.compile(r'http.+\.pdf')

    resp=urllib2.urlopen(link)
    t=resp.read()
    title=rrTitle.findall(t)[0][25:-1]

    pdfLink=rrPDF.findall(t)[0]

    return [pdfLink,title+".pdf"]
def downPDF(link,name):
    f=urllib2.urlopen(link)
    data=f.read()
    with open(name,"wb") as code:
        code.write(data)
    return

# def func():
#     print 'func() passed to Thread'
#
# t = threading.Thread(target=func)
# t.start()

#多线程例子

# def worker(a):
#
#     print "name:"+a
#     return
#
# for i in xrange(5):
#
#     t = threading.Thread(target=worker,args=(str(i),))
#
#     t.start()

# os.mkdir("1")
# os.chdir("1")
# os.chdir("..")
# os.mkdir("2")

# arr=getCon()
# for i in arr:
#i=arr[15]
# print i[0]
# print i[1]
i=['http://calculus.yuyumagic424.net/?cat=29', '\xe9\xab\x98\xe4\xb8\xad\xe6\x95\xb8\xe5\xad\xb8']
l=getCteLink(i[0])
# os.mkdir(i[1])
# os.chdir(i[1])
for m in l:
    print m
    # a = getPDFandNAME(m)
    # try:
    #     downPDF(a[0], a[1])
    # except Exception:
    #     pass
    # LinkName=getPDFandNAME(m)
    # if len(LinkName)>0:
    #     downPDF(LinkName[0],LinkName[1])
    # t=threading.Thread(target=downPDF,args=(LinkName[0],LinkName[1],))
    # t.start()
# os.chdir("..")

# http://calculus.yuyumagic424.net/?p=1036
# http://calculus.yuyumagic424.net/?p=1017
# http://calculus.yuyumagic424.net/?p=996
# http://calculus.yuyumagic424.net/?p=791
# http://calculus.yuyumagic424.net/?p=787
# http://calculus.yuyumagic424.net/?p=763
# http://calculus.yuyumagic424.net/?p=755
# http://calculus.yuyumagic424.net/?p=747
# http://calculus.yuyumagic424.net/?p=744


#getPDFandNAME('http://calculus.yuyumagic424.net/?p=980')

#['http://calculus.yuyumagic424.net/wp-content/uploads/2018/01/12-06-\xe7\x90\x83\xe5\x9d\x90\xe6\xa8\x99\xe4\xbb\xa3\xe6\x8f\x9b.pdf', '\xe7\x90\x83\xe5\x9d\x90\xe6\xa8\x99\xe4\xbb\xa3\xe6\x8f\x9b']
#['http://calculus.yuyumagic424.net/?p=980', 'http://calculus.yuyumagic424.net/?p=976', 'http://calculus.yuyumagic424.net/?p=973', 'http://calculus.yuyumagic424.net/?p=390', 'http://calculus.yuyumagic424.net/?p=370']
#index=[['http://calculus.yuyumagic424.net/?cat=4', '00 \xe5\xbe\xae\xe7\xa9\x8d\xe5\x88\x86\xe7\x9a\x84\xe5\x9f\xba\xe7\xa4\x8e'], ['http://calculus.yuyumagic424.net/?cat=3', '01 \xe6\xa5\xb5\xe9\x99\x90\xe8\x88\x87\xe9\x80\xa3\xe7\xba\x8c'], ['http://calculus.yuyumagic424.net/?cat=5', '02 \xe5\xbe\xae\xe5\x88\x86'], ['http://calculus.yuyumagic424.net/?cat=6', '03 \xe5\xbe\xae\xe5\x88\x86\xe7\x9a\x84\xe6\x87\x89\xe7\x94\xa8'], ['http://calculus.yuyumagic424.net/?cat=7', '04 \xe7\xa9\x8d\xe5\x88\x86'], ['http://calculus.yuyumagic424.net/?cat=8', '05 \xe7\xa9\x8d\xe5\x88\x86\xe6\x8a\x80\xe5\xb7\xa7'], ['http://calculus.yuyumagic424.net/?cat=10', '06 \xe7\xa9\x8d\xe5\x88\x86\xe7\x9a\x84\xe6\x87\x89\xe7\x94\xa8'], ['http://calculus.yuyumagic424.net/?cat=16', '07 \xe7\x89\xb9\xe6\xae\x8a\xe5\x87\xbd\xe6\x95\xb8'], ['http://calculus.yuyumagic424.net/?cat=9', '08 \xe7\x84\xa1\xe7\xaa\xae\xe7\xb4\x9a\xe6\x95\xb8'], ['http://calculus.yuyumagic424.net/?cat=14', '09 \xe6\xb3\xb0\xe5\x8b\x92\xe5\xb1\x95\xe9\x96\x8b'], ['http://calculus.yuyumagic424.net/?cat=17', '10 \xe6\xa5\xb5\xe5\xba\xa7\xe6\xa8\x99'], ['http://calculus.yuyumagic424.net/?cat=11', '11 \xe5\xa4\x9a\xe8\xae\x8a\xe5\x87\xbd\xe6\x95\xb8\xe7\x9a\x84\xe5\xbe\xae\xe5\x88\x86'], ['http://calculus.yuyumagic424.net/?cat=15', '12 \xe9\x87\x8d\xe7\xa9\x8d\xe5\x88\x86'], ['http://calculus.yuyumagic424.net/?cat=12', '\xe5\x85\xb6\xe5\xae\x83\xe4\xba\x8b\xe9\xa0\x85'], ['http://calculus.yuyumagic424.net/?cat=1', '\xe6\x9c\xaa\xe5\x88\x86\xe9\xa1\x9e'], ['http://calculus.yuyumagic424.net/?cat=29', '\xe9\xab\x98\xe4\xb8\xad\xe6\x95\xb8\xe5\xad\xb8']]
#os.mkdir(str(index[0][1]))
#os.chdir(str(index[0][1]))
