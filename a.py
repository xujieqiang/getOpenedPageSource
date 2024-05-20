
import datetime
import requests
import os
start=datetime.datetime.now()
a=[]
for i in range(1001):
    a.append(i)
end=datetime.datetime.now()
print(end-start)

page=requests.get('https://cn.bing.com')
print(page.text)

os.system("start C:/\"Program Files\"/Google/Chrome/Application/chrome.exe   --remote-debugging-port=9222")