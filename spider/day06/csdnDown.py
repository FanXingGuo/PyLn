import requests
from lxml import etree
#from flask import render_template,request
import re
import zlib



pageurl='https://download.csdn.net/download/cnmiss/931875'
#downurl='https://download.csdn.net/index.php/vip_download/download_client/10676310'



def downFile(pageurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Cookie": 'uuid_tt_dd=-6479278078459034903_20170309; _ga=GA1.2.1386083434.1489144919; ADHOC_MEMBERSHIP_CLIENT_ID1.0=27a368d7-dcf0-5c6f-a25d-59699c4411f2; _uab_collina=151097961707772407399296; download_first=1; UN=cyzyfs; UE="study1997.fxg@hotmail.com"; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; kd_user_id=fd1ebe34-a48b-486b-a178-73cafe6a676c; __yadk_uid=17y2aXSy1QAyeUFOxDOgk9znRepUTI7e; __utma=17226283.1386083434.1489144919.1510581765.1520249548.6; smidV2=20180607151022f8f01ce728ecea0bbc89130bd8dec58c006221ecd0c954790; UserName=cyzyfs; UserInfo=vAB7q7Hh4YFw7caux4q%2FV4pK%2ByRjwblWh3y4t%2Fw2%2B6WO5dgZ1CqNvf9%2FwXcohu5EnV8l4%2BizfmlUL7r86%2Bm0H3AlS5LMtguJVu4hQn79Q%2BvHU4%2F6aZpKq1jxqNLqVxtrk%2FIsT%2BDynoVD%2BDHwOKTgMQ%3D%3D; UserNick=%E8%8C%B6%E7%83%9F%E7%AB%B9%E9%9F%B5%E9%A3%8E%E5%A3%B0; AU=D19; BT=1536828804328; UserToken=vAB7q7Hh4YFw7caux4q%2FV4pK%2ByRjwblWh3y4t%2Fw2%2B6WO5dgZ1CqNvf9%2FwXcohu5EnV8l4%2BizfmlUL7r86%2Bm0H3AlS5LMtguJVu4hQn79Q%2BvHU4%2F6aZpKq1jxqNLqVxtrfcDJyXNzk9RMcAhJ%2FpvJBYlQiYR5ip2ocLnwY594DXG1xGoKsEpJDQlkY0XfwgV8; ARK_ID=JS8740ceefbf23bf29e07a1764f5e6a2c68740; dc_session_id=10_1537319072915.569439; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1537282436,1537319077,1537327320,1537342161; _umdata=55F3A8BFC9C50DDA84692E5451AB45757C7EC4134BA6FF1D13388886A52F8F0A7EDD5FF032007A5ACD43AD3E795C914C524559AB44A2BBEFD9E999008AA26476; PHPSESSID=93e39889f3908230d7b1d69c48e35dd7; TY_SESSION_ID=96ac986b-a49f-4cad-aaa4-324dca2bd8e6; dc_tos=pfalgv; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1537343024; ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2287f76ba9e1a77bba47f296d6e0ad9098%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A15%3A%22120.202.181.143%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A120%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_6%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F69.0.3497.100+Safari%2F537.3%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1537343030%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22userInfo%22%3Ba%3A8%3A%7Bi%3A0%3Bs%3A8%3A%2264393393%22%3Bi%3A1%3Bs%3A6%3A%22cyzyfs%22%3Bi%3A2%3Bs%3A32%3A%221b745ee4456f93ab87e7bac6c6bab458%22%3Bi%3A3%3Bs%3A25%3A%22study1997.fxg%40hotmail.com%22%3Bi%3A4%3Bs%3A1%3A%221%22%3Bi%3A5%3Bs%3A1%3A%220%22%3Bi%3A6%3Bs%3A21%3A%222016-10-10+22%3A23%3A28.0%22%3Bi%3A7%3Bs%3A1%3A%220%22%3B%7D%7Db76311748e76f61a592b31e8d14df961',
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    #根据网页获取下载地址
    resp=requests.get(pageurl,headers=headers)
    html=resp.content.decode("utf-8")
    #获取真正的下载地址 r.url 以及内容 r.content
    htmlEle=etree.HTML(html)
    downurl=htmlEle.xpath("//a[@id='vip_btn']/@href")[0]
    r=requests.get(downurl,headers=headers)
    #尝试通过响应头获取文件名 因 编码问题 未获取到
    # filename=r.headers['Content-Disposition']
    # filename=str(filename).encode("utf-8")
    # filename=filename.decode("utf-8")
    # print(filename)
    #print(bytes(filename).decode('utf-8'))
    #print(filename.split('"')[-2])
    # print(r.url)
    #//a[@id='vip_btn']/@href
    #根据网页内容获取文件类型(realType) 和文件名(fileName) =name
    #文件类型
    fileEle=htmlEle.xpath("//dl[@class='download_dl']//img/@title")[0]
    fileType=re.match(r'[a-z]+',fileEle).group()
    realType="."+fileType
    #文件名称
    filenName=htmlEle.xpath("//dl[@class='download_dl']/dd/h3/@title")[0]
    #组装文件名
    name=filenName+realType
    #根据下载地址,下载文件
    filePath="/usr/local/nginx/html/csdnData/"
    fileUrl="http://47.106.209.59/csdnData/"

    with open(filePath+name,'wb') as file:
        file.write(r.content)
    file.close()

    return fileUrl+name

