"""
#study_re match
import re

p = re.compile('[a-z]+')

m = p.match("python")
print(m)

m = p.match("3 python")
print(m)
"""

"""
p = re.compie(정규표현식)
m = p.match("조사할 문자열")

if m:
    print('Match found: ', m.group())
else:
    print('No match')
"""
"""
#study_re search

import re
p = re.compile('[a-z]+')

m = p.search("python")
print(m)

m = p.search("3 python")
print(m)
"""             
"""
#study_re. py finditer

import re

p = re.compile('[a-z]+')

result = p. finditer("life is too short")
print(result)

for r in result: print(r)
"""
"""
#study_re.py     method

import re
p = re.compile('[a-z]+')
m = p.match("python")
#에디터에서는 그냥하면 안 보이므로 프린트 넣어줘야 함
#셸에선 될 수도?
print(m.group())
m.start()
m.end()
print(m.span())

m = p.search("3 python")
print(m.group())
m.start()
m.end()
print(m.span())
"""
"""
#study_re.py
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
#None

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)
#<re.Match object; span=(0, 3), match='a\nb'>

"""

"""
#study_re.py  IGNORE

import re

p = re.compile('[a-z]+', re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')
"""
"""
#study_re.py MULTILINE

import re

p = re.compile("^python\s\w+", re.MULTILINE)
#긱 라인의 처음에 python이 오고 그 뒤에 스페이스 한 번 +문자반복된 것  찾기


#data = """#python one
#life is too short
#python two
#you need python
#python three"""

#print(p.findall(data))


#study_re.py MULTILINE + 번외

import re

p = re.compile("^python\s\w*", re.MULTILINE)
#긱 라인의 처음에 python이 오고 그 뒤에 스페이스 한 번 +문자반복된 것  찾기

data = """python one
life is too shor
python 
you need python
python three"""

print(p.findall(data))
