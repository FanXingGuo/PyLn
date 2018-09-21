import re
from lxml import etree

def getValue(text):
    chLen=len(re.findall(r'[\u4E00-\u9FFF]',text))
    pLen=len(re.findall('</p>',text))
    aLen=len(re.findall('<',text))
    equLen=len(re.findall("=",text))
    httpLen=len(re.findall("http",text))
    return (chLen*pLen)/(1.0*(httpLen+equLen*aLen))


def getContent(html):
    htmlEle = etree.HTML(html)
    part = htmlEle.xpath("//div")
    result = []
    textList = []

    for index, item in enumerate(part):
        strs = etree.tostring(item, encoding="utf-8", pretty_print=True, method="html")
        text = str(strs, encoding="utf-8")
        textList.append(text)
        result.append((index, getValue(text)))

    result = sorted(result, key=lambda a: a[1], reverse=True)

    return textList[result[0][0]]


if __name__=="__main__":
    import requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    url = 'http://www.ce.cn/cysc/tech/gd2012/201809/20/t20180920_30353367.shtml'
    html = requests.get(url, headers=headers).content.decode("gb2312")

    print(getContent(html))