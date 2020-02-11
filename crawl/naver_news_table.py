#naver_news_table.py


import urllib.request
import bs4
import sqlite3
import time

"""
#커서 생성
con = sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()


cur.execute("DROP TABLE newsTable")
cur.execute("CREATE TABLE newsTable (Div char(10), Title char(100), Writer char(10))")
"""

##변수 선언 부분
con, cur = None, None
data1, data2, data3, data4, data5 = "", "", "", "", ""
sql = ""

#메인 코드부분
con = sqlite3.connect("C:/sqlite/naverDB")
cur = con.cursor()



while True:
    url = "https://news.naver.com/"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")  # 크롤링한 거 깔끔하게 정리
    # print(bs_obj)

    hdline_article_list = bs_obj.find("ul", {"class": "hdline_article_list"})
    # print(hdline_article_list)

    lis = hdline_article_list.findAll("li")
    i = 0
    for li in lis:
        i += 1
        a_tag = li.find("a")
        headline = a_tag.text
        headline = headline.strip()
        #print(headline.strip())

        #data1 = i
        #print(i)
        data2 = "정치"
        data3 = headline.replace("'", " ")
        data3 = data3.replace('"', " ")
        print(data3)
        data4 = "jwlee"
        #data5 = time.time()

        sql = "INSERT INTO newsTable VALUES('" + data2 + "','" + data3 + "', '" + data4 + "')"
    break
#cur.execute("INSERT INTO NEWS VALUES()")



cur.execute(sql)
