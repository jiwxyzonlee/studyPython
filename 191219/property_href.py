#property_href.py
import bs4

html_str = """
<html>
    <body>
        <ul class = "ko">
            <li>
                <a href = "https://www.naver.com/">네이버</a>
            </li>
            <li>
                <b href = "https://www.daum.net/">다음</b>
            </li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
atag = bs_obj.find("a")
#atag1 = bs_obj.findAll("a")
#print(atag1)
btag = bs_obj.find("b")

print(atag.text)
print(atag)
print(btag.text)
print(btag)

#속성값 뽑기
print(atag['href'])
print(btag['href'])

