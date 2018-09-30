import requests
from lxml import etree
headers = {

    "Connection": "keep-alive",
    "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8",

}

url="https://www.thepaper.cn/newsDetail_forward_2491159"

html=requests.get(url,headers=headers).content.decode("utf-8")
#print(html)
htmlEle=etree.HTML(html)
news_title=htmlEle.xpath("//div[@class='newscontent']/h1/text()")
news_path=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_path"]/a//text()')
news_about=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_about"]/p//text()')
news_txt=htmlEle.xpath('//div[@class="news_txt"]//text()|//div[@class="news_txt"]/div/img/@src')
news_imgInfo=htmlEle.xpath('//div[@class="news_txt"]/span/text()')
news_editor=htmlEle.xpath("//div[@class='newscontent']/div[@class='news_editor']/text()")
news_keywords=htmlEle.xpath('//div[@class="newscontent"]/div[@class="news_keyword"]/text()')

print(news_title)
print("=== ==="*20)
print(news_path)
print("=== ==="*20)
print(news_about)
print("=== ==="*20)
for item in news_txt:
    print(item)
    print("=== ===" * 20)
print("=== ==="*20)
print(news_editor)
print("=== ==="*20)
print(news_keywords)
print("=== ==="*20)
#对于图片信息 获取了两次 一次在txt 一次是专门获取再info 如果图片后面的 和 info的里面的内容有一致的则为图片描述
print(news_imgInfo)


