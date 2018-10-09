import requests
url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1539006760310&di=f87441337ca181ffa65ca743859a5874&imgtype=0&src=http%3A%2F%2Fg.hiphotos.baidu.com%2Fexp%2Fw%3D500%2Fsign%3D01cfc7349516fdfad86cc6ee848f8cea%2F4034970a304e251f33ead8e7af86c9177f3e538b.jpg"
resp = requests.get(url)
with open("2.jpg","wb") as file:
    file.write(resp.content)



