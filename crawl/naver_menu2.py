#naver_menu2.py

import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리(파싱)
ul = bs_obj.find("ul", {"id":"PM_ID_serviceNavi"})
#print(ul)
#<ul id="PM_ID_serviceNavi">    개발자 도구 더 보기에서 디렉토리 확인
#<li class="an_item">


lis = ul.findAll("li", {"class":"an_item"})  #그냥 find로 찾으면 중간에 공백생겨서 리스트에 담김
#print(lis)
#<li class="an_item"> 디렉토리 아래 '메일' 태그 종류 확인
#<span class="an_txt">메일</span></a>


for li in lis:      #<li>마다 있는 "a"태그 찾기(리스트에서 하나씩 꺼내서)
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)
