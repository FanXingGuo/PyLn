import requests
from bs4 import BeautifulSoup
import re
headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}
url='https://www.cnbeta.com/articles/770035.htm'

html=requests.get(url,headers=headers).content.decode('utf-8')

soup=BeautifulSoup(html,"html.parser")
part=soup.select("div")




def countchn(string):
    #统计中文字符数
    pattern = re.compile(u'[\u1100-\uFFFDh]+?')
    result = pattern.findall(string)
    chnnum = len(result)            #list的长度即是中文的字数

    possible = chnnum/len(str(string))         #possible = 中文字数/总字数
    return (chnnum, possible)

def findtext(part):
    length = 50000000
    l = []
    for paragraph in part:
        chnstatus = countchn(str(paragraph))
        possible = chnstatus[1]
        if possible > 0.15:
            l.append(paragraph)
    l_t = l[:]
    #这里需要复制一下表，在新表中再次筛选，要不然会出问题，跟Python的内存机制有关
    for elements in l_t:
        chnstatus = countchn(str(elements))
        chnnum2 = chnstatus[0]
        if chnnum2 < 300:
        #最终测试结果表明300字是一个比较靠谱的标准，低于300字的正文咱也不想要了对不
            l.remove(elements)
        elif len(str(elements))<length:
            length = len(str(elements))
            paragraph_f = elements
    return paragraph_f
