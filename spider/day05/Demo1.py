from selenium import webdriver
from lxml import etree
from pyquery import PyQuery as pq
import time

#头条文章 目录 , 目录链接未处理重定向

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toutiao.com/')
driver.implicitly_wait(10)
driver.find_element_by_link_text('科技').click()
driver.implicitly_wait(10)
for x in range(180):
    js="var q=document.documentElement.scrollTop="+str(x*1000)
    driver.execute_script(js)
    time.sleep(1)
    print(x)

time.sleep(5)
page = driver.page_source
doc = pq(page)
doc = etree.HTML(str(doc))
contents = doc.xpath('//div[@class="wcommonFeed"]/ul/li')
print(contents)
for x in contents:
    title = x.xpath(".//div[@class='title-box']/a/text()")
    link=x.xpath(".//a[@class='link title']/@href")


    if title :
        title = title[0]
        link=link[0]
        if link.startswith("/group"):
            link='https://www.toutiao.com/'+link
        else:
            continue
        ct={"title":title,"link":link}
        with open('toutiao.txt','a+',encoding='utf8')as f:
            f.write(str(ct)+'\n')
        print(str(ct))

    else:
        pass

driver.quit()