#naver_headline.py


import urllib.request
import bs4
import time

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리
#print(bs_obj)

hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
#print(hdline_article_list)

lis = hdline_article_list.findAll("li")

while True:
    for li in lis:
        a_tag = li.find("a")
        headline = a_tag.text
        print(headline.strip())  #공백이 양쪽으로 있었음
    time.sleep(60)
