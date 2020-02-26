#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests 
#requests가 가지고 있는 것들을 현재 커널에 requests 라는 이름으로 가져옴

#get 요청을 해서 텍스트를 확인
resp = requests.get('http://httpbin.org/get')

#help(requests.get) #함수의 도움말 확인

#print(type(resp)) #리턴된 결과의 자료형을 확인
#print(dir(requests.models.Response)) #Response 자료형은 어떤 속성들을 가졌는지 확인

print(resp.text) #가져온 문자열을 확인


# In[8]:


#put 과 delete 요청
resp = requests.put('http://httpbin.org/put')
print(resp.text)
print()
resp = requests.delete('http://httpbin.org/delete')
print(resp.text)


# In[10]:


#help(requests.post)
#requests 모듈을 사용하면 파라미터 인코딩을 할 필요가 없습니다.
resp = requests.post('http://httpbin.org/post', data={'name':'박문석', 'num':1})
print(resp.text)


# In[11]:


#Kakao Open API 도서 검색 사용
addr = 'https://dapi.kakao.com/v3/search/book'
params = {'query':'삼국지', 'target':'title'}
headers = {'Authorization': 'KakaoAK 228e2b377f259ec5a956a267b27ded62'}
resp = requests.get(addr, params=params, headers=headers)
print(resp.text)


# In[14]:


#이미지를 다운로드 받아서 파일로 만들기

#이미지를 가져올 URL을 생성
imgurl = 'http://www.onlifezone.com/files/attach/images/962811/376/321/005/2.jpg'

resp = requests.get(imgurl)

#파일 객체를 만들고 이름은 f로 사용 - close를 할 필요가 없습니다.
with open('2.jpg', 'wb') as f:
    f.write(resp.content)
    
#현재 작업디렉토리 확인
import os
print(os.getcwd())
    


# In[ ]:





# In[9]:


#웹에서 정적인 데이터를 가져오기 위한 라이브러리를 import
import requests

#다운로드 받을 URL 만들기
addr = 'https://dapi.kakao.com/v2/local/search/category.json?category_group_code=FD6&rect=127.0561466,37.5058277,127.0602340,37.5142554'

#header 만들기
headers = {'Authorization': 'KakaoAK 228e2b377f259ec5a956a267b27ded62'}

#데이터 가져와서 출력
resp = requests.get(addr, headers=headers)
text = resp.text
#print(text)

#json 파싱 모듈을 가져오기 - 내장 모듈
import json
jsondata = json.loads(text)
#print(type(jsondata)) #맨 처음 시작이 {} 이므로 dict

#print(jsondata['documents']) #documents 키의 데이터 가져오기 - list
li = []
#가져온 배열을 행 단위로 읽어서
for imsi in jsondata['documents']:
    #print(imsi['address_name'], ':', imsi['place_name'])
    #place_name 과 address_name을 가지고 dict를 생성
    d = {'장소':imsi['place_name'], '주소':imsi['address_name']}
    #dict를 list에 추가
    li.append(d)

#확인
for temp in li:
    print(temp)


# In[ ]:





# In[20]:


#위키피디아에서 하이퍼링크(a) 태그의 내용 가져오기
import requests

addr = 'https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5'
resp = requests.get(addr)
#print(resp.text)

#html 파싱을 위한 라이브러리 가져오기
import bs4

#DOM 객체로 만들기
bs = bs4.BeautifulSoup(resp.text, 'html.parser')
#print(type(bs))

#a 태그의 내용 가져오기
li = bs.find_all('a')
#print(li)

#정규식(문자열 패턴을 조회하기 위한 식) 모듈 import
import re
for temp in li:
    #print(temp.getText()) #태그 안의 내용 가져오기
    #print(temp.attrs['href']) #key 에러 - href가 없는 경우도 있음
    if 'href' in temp.attrs: #href 속성이 temp.attrs에 있는 경우에만
        #href 속성에 /wiki/로 시작하는 링크의 텍스트와 링크만 출력
        href = temp.attrs['href']
        #정규식 생성 - /wiki/ 로 시작하는
        p = re.compile('^(/wiki/)')
        if p.search(href) != None:
            print(temp.getText(), ':', href)
    


# In[28]:


#네이버 tv 팟에서 하이퍼링크(a) 태그의 내용 가져오기
import requests

addr = 'https://tv.naver.com/'
resp = requests.get(addr)
#print(resp.text)

#html 파싱을 위한 라이브러리 가져오기
import bs4

#DOM 객체로 만들기
bs = bs4.BeautifulSoup(resp.text, 'html.parser')
#선택자를 이용해서 선택
tvlist = bs.select('dl > dt > a > tooltip')
for temp in tvlist:
    print(temp.getText())


# In[44]:


#오늘 날씨를 가져와서 그래프 그리기
import requests

#필요한 html 가져오기
resp = requests.get('http://www.weather.go.kr/weather/observation/currentweather.jsp')
text = resp.text
#print(text)

import bs4
bs = bs4.BeautifulSoup(text, 'html.parser')
#class 속성의 값이 table_develop3 인 데이터 찾아오기
table = bs.select('.table_develop3')
#print(table)

#도시이름, 온도, 습도를 저장할 list를 생성
loc = []
temp = []
hum = []

#가져온 테이블 중에서 첫번째 테이블로부터 줄(tr) 단위로 읽기
for tr in table[0].find_all('tr'):
    tds = tr.find_all('td') #tr 태그에서 td를 전부 찾아서 tds에 대입
    for td in tds:
        if td.find('a'): #a 태그가 있으면 도시이름이 있는 행입니다.
            #도시이름을 loc 추가
            loc.append(td.find('a').text)
            #온도를 temp에 추가
            temp.append(tds[5].text)
            #습도를 temp에 추가
            hum.append(tds[10].text)

#데이터 확인
#인덱싱은 번호1개만 작성해서 하나의 데이터만 추출
print(loc[0:5]) #0-4 번행 까지 확인 - 슬라이싱(범위를 가지고 추출)
print(temp[0:5])
print(hum[0:5])

#필요한 도시의 데이터만 추출
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '창원', '흑산도']
#위 도시들의 온도와 습도를 저장할 list
temperatures = []
humidities = []

#cities에 있는 데이터만 추출해서 저장
for city in cities:
    j = 0
    for c in loc:
        if c == city:
            temperatures.append(temp[j])
            humidities.append(hum[j])
            break
        j = j + 1

print(cities)
print(temperatures)
print(humidities)

#파이썬에서 시각화를 하는 기본 패키지
import matplotlib.pyplot as plt 
#한글 폰트 사용을 위한 패키지
from matplotlib import font_manager, rc, rcParams
import platform #운영체제 확인을 위한 패키지

#주피터 노트북에서 그래프를 셀 안에 출력해주는 설정
get_ipython().run_line_magic('matplotlib', 'inline')

#음수를 제대로 표현하기 위한 설정
rcParams['axes.unicode_minus'] = False #이 설정을 하지 않으면 음수가 네모로 출력

#한글 폰트 설정
if platform.system() == 'Windows': #윈도우즈라면
    font_name = font_manager.FontProperties(fname='c:/windows/Fonts/ahn_b.ttf').get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin': #매킨토시라면
    rc('font', family='AppleGothic')
else:
    print('알 수 없는 운영체제')
    
    
#그래프 그리기
plt.figure(figsize=(12,4), dpi=300) #그래프 크기 설정 - 가로 12inch 세로 4인치
#꺽은선 그래프 - plot
plt.plot(temperatures, label='온도', lw=3, color='r', linestyle='-', marker='s')
#plt.plot(humidities, label='습도', lw=3, color='g', linestyle='-', marker='s')

#x 축
plt.xticks(range(0,len(cities),1), cities, rotation='vertical')
#범례
plt.legend()
plt.savefig('graph.png', dpi=300)
#출력
plt.show()


# In[ ]:





# In[46]:


#XML 파싱
#http://www.hani.co.kr/rss/ 에서 item 태그의 title만 추출

#데이터 가져오기
import requests
resp = requests.get('http://www.hani.co.kr/rss/')
text = resp.text
#print(text)

import bs4
#트리로 펼쳐내기
bs = bs4.BeautifulSoup(text, 'lxml-xml')

items = bs.find_all('item')

for item in items:
    title = item.find('title')
    print(title.getText())


# In[ ]:





# In[2]:


#크롬 실행하기
from selenium import webdriver
driver = webdriver.Chrome('c:/chromedriver')


# In[3]:


#다음 카페 목록에 접근하기
#크롬 실행하기
from selenium import webdriver
driver = webdriver.Chrome('c:/chromedriver')
#3초대기
driver.implicitly_wait(3)

#다음 카페 목록에 접근 - 로그인 되어 있지 않으면 로그인 페이지로 이동
driver.get('http://top.cafe.daum.net/_c21_/my_cafe')


# In[16]:


#다음에 로그인을 하고 카페 목록으로 이동
from selenium import webdriver
#크롬을 화면에 출력하지 않고 실행하기
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('c:/chromedriver', chrome_options=options)

#driver = webdriver.Chrome('c:/chromedriver')

#3초대기
driver.implicitly_wait(3)

#다음 로그인 페이지로 이동
driver.get('https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F')

#아이디와 비밀번호 입력받기
username = input('아이디를 입력하세요')
userpw = input('비밀번호를 입력하세요')

#다음 로그인 페이지에 아이디와 비밀번호 입력
#driver.find_element_by_id('id').send_keys(username)
driver.find_element_by_xpath('//*[@id="id"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="inputPwd"]').send_keys(userpw)

driver.find_element_by_xpath('//*[@id="loginBtn"]').click()

#여러 페이지를 이동할 때는 중간에 잠시 대기 시간을 주어야 할 필요가 있습니다.
import time
time.sleep(3) #3초 대기

#카페 목록 페이지로 이동
driver.get('http://top.cafe.daum.net/_c21_/my_cafe')
time.sleep(3)
#카페 목록 중에서 첫번째 페이지로 이동
#driver.find_element_by_xpath('//*[@id="mArticle"]/div/div[1]/div/div[2]/ul/li/a/div[1]/div[2]/div/div/strong').click()

#직접 카페로 이동 - 카페 글쓰기 페이지로 이동
driver.get('http://cafe.daum.net/samhak7/_memo')

#특정 프레임으로 이동
driver.switch_to_frame('down')

#글작성 란에 텍스트를 입력
driver.find_element_by_xpath('//*[@id="memoForm"]/div/table/tbody/tr[1]/td[1]/div/textarea').send_keys('파이썬에서의 매크로')
driver.find_element_by_xpath('//*[@id="memoForm"]/div/table/tbody/tr[1]/td[2]/a[1]/span[2]').click()


# In[ ]:





# In[17]:


#20번 스크롤 하기
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import bs4

driver = webdriver.Chrome('c:/chromedriver')

driver.get('https://www.youtube.com/results?search_query=%EB%A7%88%EB%A7%88%EB%AC%B4')
time.sleep(5)

body = driver.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출
num_of_pagedowns = 20
#10번 밑으로 내리는 것
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)
    num_of_pagedowns -= 1
    
html = bs4.BeautifulSoup(driver.page_source,'html.parser')
print(html)

