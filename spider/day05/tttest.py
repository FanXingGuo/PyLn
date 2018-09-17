import requests

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'www.toutiao.com',
'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
'Connection': 'keep-alive',
'Accept-Language': 'zh-cn',
'Accept-Encoding': 'br, gzip, deflate',
'Cookie': 'tt_webid=6602081668931503623; CNZZDATA1259612802=1619642678-1537166455-%7C1537166455; __tasessionId=8uih9u68z1537166925808; csrftoken=45e5b88ee470a86091a88da3a2b174b2; UM_distinctid=165e649df4a664-0b547897727d6d-49183707-fa000-165e649df4ba2e; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6602081668931503623; _ga=GA1.2.923123784.1477571966; uuid="w:12db9b25e32944f1bf6967e65282fe2f"',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
'Referer': 'https://www.toutiao.com/ch/news_finance/',
'X-Requested-With':'XMLHttpRequest',
}
url='https://www.toutiao.com/group/6599794816995820046/'
response=requests.get(url)
print(response.content.decode('utf-8'))

# url='https://www.toutiao.com/api/pc/feed/'
# data={
# 'category':'news_hot',
#  'utm_source':'toutiao',
#  'widen':'1',
#  'max_behot_time':'1537102845',
#  'max_behot_time_tmp':'1537102845',
# 'tadrequire':'true',
#  'as':'A1B5BB897EB5CB3',
#  'cp':'5B9E05CC9B734E1',
#  '_signature':'4XAtaAAAuvleBtyOe6LPu-FwLX',
# }
# resp=requests.get(url,headers=headers,params=data)
# cont=resp.content.decode('utf-8')
# print(cont)