#encoding:utf-8
from selenium import webdriver
import time
from urllib import request

TextCt=['http://p3.pstatp.com/large/pgc-image/1535344004560f423953b48', '作为一个拥有阿里巴巴背景，功能又丰富多样的办公室软件，钉钉一直受到很多公司行政部门和管理层的青睐。', '尤其是一些互联网公司里面，恨不得把所有的工作尽可能地都和钉钉拉上关系。', '但与此同时，在上班族的口中，这个软件却显得很不友好——无休无止的“钉一下”、各种花式折腾流程、总是感觉自己被监控的阅读回执。', '在某些问答网站里面，关于钉钉的差评几乎是一面倒的，随意翻开一个问题，似乎有70%以上的回答都是反对的。', '甚至有些网友提出了“离职以后第一件事情就是卸载钉钉”、“面试的时候可以通过问公司用不用钉钉来判定这是不是一个恶心的企业”等说法。', '那么，究竟是什么原因，导致钉钉走上了让人深恶痛绝的道路呢？', 'http://p9.pstatp.com/large/pgc-image/1535343927819f2860a8bb0', '我们先来看看使用钉钉的三类公司：', '钉钉对这种公司来说，就是一个极度简单的功能补充软件。', '比如那些懒得买打卡机的企业，直接拿钉钉的考勤功能来记录员工上下班时间。', '还有的企业用钉钉纯粹拿来发布一些公司的通知，显得比微信和QQ要正式点，用起来又比发邮件要方便一点。', '甚至还有企业，就是把这个软件，当成更新公司通讯录的工具……', '总之，在他们眼中，钉钉就是一个很普通的软件，有了会方便一点，没有的话也无所谓。', 'http://p1.pstatp.com/large/pgc-image/15353439277628134bad6cb', '之所以叫文艺公司，是因为他们把钉钉用的太人文艺术了。', '一个定位考勤功能，让人只要到了公司楼下就感觉安全了，再也不怕买个早餐或者等个电梯就迟到一两分钟了。', '行政审批，本来要人肉跑好几个部门盖章，拿好几个领导签名的各种流程，比如申请备用金、报销、出差审批、请假等等的，只要手机上操作一下，几分钟就能解决。', '更重要的是，流程走到哪里一目了然，不然害怕不礼貌而不敢催不敢问。', '云文件，再也不用经历“我想要个文件但是我不知道找谁要，我以为他是负责人结果他告诉我没有”的事情了，大家做到一定程度的文件，就能往上丢，轻轻松松云协作。实在要在家里加班，也能很快找到自己想要是素材了。', '总之，在他们眼中，钉钉就是一个用来提升工作效率，让上班变得更轻松的软件。', 'http://p1.pstatp.com/large/pgc-image/153534392779656bce7f138', '这类就是网友们最讨厌的公司，他们的员工深深笼罩在被钉钉支配的恐惧中。', '上下班打卡还得微笑，遇到被领导批完心情很不好的时候，简直觉得自己是人格分裂。', '上班晚了一分钟算迟到，下班设置成永远不算加班。', '外勤人员隔十五分钟就要定位打卡，防止你偷懒或者干别的去了。', '一旦看到消息显示为“已读”却没有立刻反馈，就会被公开批评。', '什么事情都要“钉”你一下，睡到半夜都会突然听到那个恐怖的提示音。', '总之，在他们的老板眼里，钉钉就是一个用来让员工24小时处于自己的监视之下的公司。只要付了钱，别说你的时间，你的命都是公司的。', 'http://p99.pstatp.com/large/pgc-image/15353439278227b7ecca014', '我们经常可以看到一种说法，', '这是一个非常见仁见智的理论，但在使用钉钉这个问题上，却发挥得淋漓尽致。钉钉究竟是让人喜欢还是让人讨厌，取决于管理层究竟想要把这个软件用到什么地方和什么程度。', '我相信，如果钉钉发挥的是正面的作用，那么就算企业不用它，也会有', '的工具。反之亦然，如果它发挥着负面的作用，也总有它的替代品。', '况且有时候，领导层的需求，和基层员工其实是相差很远的。', '有网友提议说，自己下班之后就会顺手登出钉钉，对于他们来说，下班的时间就是属于自己的，绝对不会再接触和公司有关的事情。', '在我看来，这也许只能是一个美好的愿望，尤其是在互联网时代，工作和生活仿佛已经交织在一起，难以割裂，在家加班也变成了非常常见的事情。但我希望，在没有必要的情况下，每个人还是能够有自己的生活。', '这样子，才会有继续奋斗的动力。', '所以，那些大部分员工都讨厌用钉钉的公司的管理层们，也许是时候考虑一下你们的管理方式了。', '———— / END / ————', '资深新媒体人，微博职场博主，企业中层管理者', '本文为原创，版权归属人事人，抄袭必究。']


from lxml.etree import _Element

from lxml import etree

# str('num%06d'%_NUM)
TEXT_NUM=0
picNum=0

timeMy=time.localtime(time.time())
timeStr=str(timeMy.tm_year)+str("%02d"%timeMy.tm_mon)+str("%02d"%timeMy.tm_mday)



def toOrder(num):
    return str('%08d'%num)

#需要一个函数 传入文章列表,对文本保存txt,对下载




file=open("toutiao.txt",'r',encoding='utf-8')
newFile=open("clean.txt",'a+',encoding='utf-8')
list=[]
driver=webdriver.Chrome()
cont=file.readlines()

for item in cont:
    item=item.replace("\n","")
    webct=eval(item)
    driver.get(webct["link"])
    time.sleep(1)
    curt_url=str(driver.current_url)
    if curt_url.startswith("https://www.toutiao.com/a"):
        webct['link']=curt_url
        print(webct['link'])


        html=driver.page_source
        htmlEl=etree.HTML(html)
        newFile.write(str(webct) + '\n')
        #获取 info 发布信息
        info=htmlEl.xpath("//div[@class='article-sub']//text()")
        info="".join(info)
        #获取 图片和内容 信息
        arctleContent=htmlEl.xpath("//div[@class='article-content']//p/text()|//div[@class='article-content']//img/@src")
        #准备下载
        print(arctleContent)
        TEXT_NUM=TEXT_NUM+1
        filename=timeStr+str(toOrder(TEXT_NUM))+".txt"


        with open("./data/txt/"+filename,"a+",encoding="utf-8") as file:
            file.write(webct['title']+'\n')
            file.write(info+"\n")
            for pageItem in arctleContent:
                if pageItem.startswith("http"):
                    picNum=picNum+1
                    picName=timeStr+toOrder(picNum)+".jpeg"
                    request.urlretrieve(pageItem,"./data/picture/"+picName)
                    file.write("{"+picName+"}"+"\n")
                else:
                    file.write(pageItem+"\n")






    else:
        continue
    print(webct['title'])
    print(TEXT_NUM)


driver.quit()
newFile.close()
