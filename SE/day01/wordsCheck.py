
#定义数据
userText="we thought she was pretty much out of the woods"
inputText=""
#输入
print("请输入一下,内容:"+userText)
inputText=input()
#结果判断
userTextLists=userText.split()
inputTextLists=inputText.split()
rightNum=0;
wrongNum=0;
for index,userItem in enumerate(userTextLists):
    if(inputTextLists[index]==userItem):
        rightNum=rightNum+1
    else:
        wrongNum=wrongNum+1

#显示输入
print("原内容:"+userText)
print("输入内容:"+inputText)
print("单词正确数目:"+str(rightNum)+",单词错误数目:"+str(wrongNum))



# print(eval("1+(3+1)/2.0*2"))

