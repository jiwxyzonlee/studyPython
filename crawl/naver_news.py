#naver_news.py

import urllib.request
import bs4
import time
import os

import subprocess


url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리
#print(bs_obj)

div = bs_obj.find("div", {"mtype_list_wide"})
print(div)

#mlist2_no_bg = bs_obj.find("ul", {"class":"mlist2 no_bg"})
#print(mlist2_no_bg)


#lis = mlist2_no_bg.findAll("li")
#print(lis)



#while True:
#    for li in lis:
#        strong = li.find("strong")
#        print(strong.text)
#    break
    #time.sleep(10)
    #print("updating news")
    #time.sleep(2)
    #os.system("cls")

