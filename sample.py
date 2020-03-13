import requests
import re
from bs4 import BeautifulSoup as bs

data = input("検索したい文字を入力してください：")
res = requests.get("https://www.google.com/search?q=" + data)

res = res.text
soup = bs(res,"html.parser")

#tags = soup.find_all("a")

tags = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
##for i in tags:
##    if(i.find("div", class_="BNeawe s3v9rd AP7Wnd") != None):
##        print(i.find("a").get("href"))
##        print(i.find("div", class_="BNeawe s3v9rd AP7Wnd").string)
##        print("")
if(tags[0].find("div",class_="BNeawe s3v9rd AP7Wnd") != None): 
    title = tags[0].find("div", class_="BNeawe s3v9rd AP7Wnd").string.split('(@')[0]
    title2 = title.strip('The latest Tweets from')
    print(title2)
    print(tags[0].find("div", class_="BNeawe s3v9rd AP7Wnd").string)
