import requests
from selenium import webdriver
import  time
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
import os
from bs4 import BeautifulSoup


os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="d:\selenium"')

import win32ui,win32con,pythoncom,win32gui
input("....")

chrome_options=Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
chrome_driver="chromedriver.exe"
driver=webdriver.Chrome(options=chrome_options)
# options = uc.ChromeOptions()
# chromedriver_path = "chromedriver.exe"
# options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
# driver = uc.Chrome(executable_path=chromedriver_path, options=options)

# print("浏览器标题",driver.title)
# print("body",driver.page_source)
html=driver.page_source

soup=BeautifulSoup(html,"html.parser")
s_title=soup.find("title")
print(s_title)
s_body=soup.find("body")
print(s_body)
