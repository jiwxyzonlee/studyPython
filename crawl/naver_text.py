#naver_text.py
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리
top_right = bs_obj.find("div", {"class":"area_links"})
#print(top_right)

first_a = top_right.find("a")
print(first_a.text)