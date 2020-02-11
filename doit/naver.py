# <웹크롤링해서 sqlite에 table 생성> #

import sqlite3
import urllib.request
import bs4
import time

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3 = "", "", ""
sql,sql2 = "",""

## 메인 코드 - 헤드라인 ##

while True:
    url = "http://news.naver.com/"
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    #on = sqlite3.connect("C:/sqlite/naverDB")
    cur = con.cursor()


#헤드라인,정치, 경제, 사회, 생활문화, 세계, IT과학

    #헤드라인
    div = bs_obj.find("div", {"id": "today_main_news"})
    hdline_article_list = div.find("ul", {"class": "hdline_article_list"})
    lis_hd = hdline_article_list.findAll("li")

    for li1 in lis_hd:
        a_tag1 = li1.find("a")
        headline = a_tag1.text.strip()

        data1 = "헤드라인"  # 뉴스 구분
        data2 = headline.replace("'", "\"")  # 뉴스 제목
        data3 = "jwlee"                      #작성자

        sql = "INSERT INTO news VALUES(datetime(),'" + data1 + "', '" + data2 + "', '" + data3 + "')"
        print(sql)

        #cur.execute(sql)

    #정치, 경제, 사회, 생활문화, 세계, IT과학
    mlist2_no_bg = bs_obj.findAll("ul", {"class":"mlist2 no_bg"})
    #print(mlist2_no_bg[0])

    span_list = bs_obj.findAll("span", {"class":"writing"})
    #print(span_list)




#정치, 경제, 사회, 생활문화, 세계, IT과학
    for span in span_list:
        span = span.text
    print(span)

    for li2 in mlist2_no_bg:
        strong = li2.find("strong")
        #print(strong)
        strong = strong.text
        print(strong)

        data1 = "정치"  # 뉴스 구분
        data2 = strong.replace("'", "\"")  # 뉴스 제목
        data3 = span  # 작성자


        sql2 = "INSERT INTO news VALUES(datetime(),'" + data1 + "', '" + data2 + "', '" + data3 + "')"

        #data = "%s, %s, %s, %s\n" % (time.ctime(), data1, data2, data3)
        #f = open("C:/crawl/naver.txt",'a')
        #f.write(data)
        #f.close()
        #print(data)

            #cur.execute(sql)
        #print(sql2)


    con.commit()
    con.close()
    break
    #time.sleep(3600)
