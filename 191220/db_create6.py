#-*- coding: utf-8 -*-

#C:/crawl/db_create.py

#import sqlite3


#con = sqlite3.connect("C:/sqlite/naverDB")
#cur = con.cursor()

#cur.execute("DROP TABLE news")
#cur.execute("CREATE TABLE news (wrdt date, div char(20), title char(100), writer char(20))")
#cur.execute("CREATE INDEX wrdt_idx on news (wrdt)")

#con.commit()
#con.close()


# <웹크롤링해서 sqlite에 table 생성> #

import sqlite3
import urllib.request
import bs4
import time
import sys
import io




## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3 = "", "", ""
sql,sql2 = "",""
i = 0
#f = open("C:/crawl/news2.csv", 'w')
#f.close()

# 메인 코드 부분 ##
while True:
    url = "http://news.naver.com/"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    #h4_class = bs_obj.findAll("h4", {"class":"tit-sec"})

    mlist = bs_obj.findAll("ul", {"class":"mlist2 no_bg"})

    f = open("c:/crawl/news2.csv", 'a')


    for li in mlist:
        lis = li.findAll("li")
        i += 1
        for li in lis:
            strong = li.find("strong")
            span_tag = li.find("span")
            print(strong.text, span_tag.text)

            print()
            #f = open("c:/crawl/news2.csv", 'a')

        
            data1 = i                      #뉴스 구분
            data2 = strong.text.strip()
            data2 = data2.replace("'", "\"")
            data2 = data2.replace(",", ".")     #뉴스 제목
            data3 = span_tag.text                        #작성자

            data = "%s, %s, %s, %s\n" % (time.ctime(), data1, data2, data3)
            #data = data.encode("utf-8")
            f.write(data)
            print(data)

    f.close()
    time.sleep(120)

