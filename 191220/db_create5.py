# -*- coding: euc-kr -*-

#C:/crawl/db_create.py

#import sqlite3


#con = sqlite3.connect("C:/sqlite/naverDB")
#cur = con.cursor()

#cur.execute("DROP TABLE news")
#cur.execute("CREATE TABLE news (wrdt date, div char(20), title char(100), writer char(20))")
#cur.execute("CREATE INDEX wrdt_idx on news (wrdt)")

#con.commit()
#con.close()


# <��ũ�Ѹ��ؼ� sqlite�� table ����> #

import sqlite3
import urllib.request
import bs4
import time
import sys
sys.getdefaultencoding()



## ���� ���� �κ� ##
con, cur = None, None
data1, data2, data3 = "", "", ""
sql,sql2 = "",""
i = 0
#f = open("C:/crawl/news2.csv", 'w')
#f.close()

# ���� �ڵ� �κ� ##
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


            data1 = i                      #���� ����
            data2 = strong.text.strip()
            data2 = data2.replace("'", "\"")
            data2 = data2.replace(",", ".")     #���� ����
            data3 = span_tag.text                        #�ۼ���

            data = "%s, %s, %s, %s\n" % (time.ctime(), data1, data2, data3)
            #data = data.encode("utf-8")
            try:
                f.write(data)
                print(data)
            except UnicodeEncodeError:
                pass

    f.close()
    time.sleep(60)

