import urllib.request
import bs4
import time

# 메인 코드 부분 ##
while True:
    url = "http://news.naver.com/"
    html = urllib.request.urlopen(url)

    bs_obj = bs4.BeautifulSoup(html, "html.parser")

    hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
    lis = hdline_article_list.findAll("li")

    f = open("c:/crawl/news.txt", 'a')

    for li in lis:
        a = li.find("a")
        a.text.strip()

        data1 = "정치"                      #뉴스 구분
        data2 = a.text.strip()
        data2 = data2.replace("'", "\"")
        data2 = data2.replace(",", ".")     #뉴스 제목
        data3 = "ydgil"                     #작성자

        data = "%s, %s, %s, %s\n" % (time.ctime(), data1, data2, data3)
        f.write(data)
        print(data)

    f.close()
    time.sleep(3600)
