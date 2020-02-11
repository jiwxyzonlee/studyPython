#find_li.py

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
body = bs_obj.find("body")
ul = body.find("ul")
li = ul.find("li")
print(bs_obj)
print(body)
print(ul)
print(li)