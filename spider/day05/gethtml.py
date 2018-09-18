import requests


newFile=open("clean.txt",'r',encoding='utf-8')
cont=newFile.readlines()
list=[]
for item in cont:
    item=item.replace("\n","")
    wk=eval(item)
    print(wk["link"])