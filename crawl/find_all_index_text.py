#find_all_index_text.py

import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
lis = ul.findAll("li")

#print(lis[1].text)

l = len(lis)
for i in range(0, l):
    print(lis[i].text)


for i in lis:
    print(i.text)
