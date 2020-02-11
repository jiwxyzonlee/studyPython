#url_open.py

from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)
# 크롤링의 과정
# 페이지를 불러온다
# urllib.request를 써서 불러온다
# urlopen(url)을 쓴다

# 파싱을 한다
# bs4.BeautifulSoup으로 파싱을 한다.
# 개발자 도구를 켜서 원하는 데이터가 있는 위치를 찾는다.

print(html.read())

