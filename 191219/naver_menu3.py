#naver_menu3.py

import urllib.request
import bs4


url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리(파싱)
div = bs_obj.find("div", {"class":"rolling-container"})
#print(div)
#<div class="rolling-container">    개발자 도구 더 보기에서 디렉토리 확인
#<li class="rolling-panel" role="presentation">


lis = div.findAll("li")  #그냥 find로 찾으면 중간에 공백생겨서 리스트에 담김
print(lis)
#<li class="rolling-panel" role="presentation"> 디렉토리 아래 '한글 텍스트' 태그 종류 확인



for li in lis:      #<li>마다 있는 "a"태그 찾기(리스트에서 하나씩 꺼내서)
    a_tag = li.find("a")
    print(a_tag.text)

