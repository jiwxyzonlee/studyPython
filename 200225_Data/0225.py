#!/usr/bin/env python
# coding: utf-8

# In[3]:


#필요한 모듈 import - 모듈을 가져오는 것입니다.
import urllib.request

#데이터 요청
response = urllib.request.urlopen('http://www.daum.net')
#데이터 출력
data = response.read()
#print(data)

#한글이 깨지는 경우
#웹에서 받아온 데이터가 깨지면 인코딩을 찾아서 디코딩을 해 주어야 함
encoding = response.info().get_content_charset()
html = data.decode(encoding)
print(html)


# In[6]:


#필요한 모듈 import - 모듈을 가져오는 것입니다.
import urllib.request
#urllib.parse에서 quote 만 가져오고 앞의 모듈이름은 제거
from urllib.parse import quote

addr = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=' 
    + quote('코로나')
#데이터 요청
response = urllib.request.urlopen(addr)
#데이터 출력
data = response.read()
#print(data)

#한글이 깨지는 경우
#웹에서 받아온 데이터가 깨지면 인코딩을 찾아서 디코딩을 해 주어야 함
encoding = response.info().get_content_charset()
html = data.decode(encoding)
print(html)


# In[ ]:




