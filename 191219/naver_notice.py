#naver_notice.py
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")  #크롤링한 거 깔끔하게 정리
#print(bs_obj)
area_notice = bs_obj.find("div", {"class":"area_notice"})
#print(area_notice)



h3_tag = area_notice.find("h3")
print(h3_tag.text)
"""

#print(bs_obj)

mlist2_no_bg = bs_obj.find("ul", {"class":"mlist2 no_bg"})
#print(mlist2_no_bg)

lis = mlist2_no_bg.findAll("li")
for li in lis:
    strong = li.find("strong")
    print(strong.text)
"""