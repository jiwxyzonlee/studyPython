import numpy as np

#일련 번호 형태로 배열만들기
ar = np.arange(1,13)
#3행 4열로 변경
ar = ar.reshape(3,4)

#일정한 간격을 가지고 만들기
br = np.linspace(101, 112, num=12)
br = br.reshape(3,4)

#행 방향으로 합치기
print(np.hstack([ar, br]))

#열 방향으로 합치기
print(np.vstack([ar, br]))

#Series 와 DataFrame은 현재 모듈에 포함
from pandas import Series, DataFrame
#Series 와 DataFrame을 제외하고는 pd로 접근
import pandas as pd

#Series 만들기
good1 = Series([1000, 1500, 500])
print(good1)

#데이터 접근
print(good1[0]) #1개의 데이터 접근
print(good1[0:2]) #연속된 범위의 데이터 접근
print(good1[[0,2]]) #불연속된 데이터 접근

#인덱스 설정
good1.index = ['Orange', 'Apple', 'Banana']
print(good1)
print(good1['Orange':'Banana'])
#Orange 부터 Banana까지

import numpy as np
good1 = Series([100, 200, 150, None, np.nan],
               index=['1','2','3', '5', '6'])
good2 = Series([10, 20, 10],
               index=['1','2','4'])
print(good1 + 200) #모든 요소에 200을 더함
print(good1 + good2) 
#인덱스가 동일한 데이터끼리 연산
#1과 2번은 양쪽에 같이있어서 더하기
#3과 4번은 한쪽에만 존재하기 때문 None

#디셔너리를 생성
items = {'name':['orange', 'mango'],
         'price':[2000, 2500],
         'manufacture':['korea', 'taiwan']}

#DataFrame을 생성
df = DataFrame(items)

print(df)

#디셔너리를 생성
items = {
   'name':['orange', 'mango', 'apple','banana'],
   'price':[2000, 2500, 3000, 500],
   'manufacture':['korea', 'taiwan', 'korea','vetnam']}

#DataFrame을 생성
df = DataFrame(items)

#인덱스를 직접설정
df.index = np.arange(10, 50, 10)
#3개의 데이터 확인
print(df.head(3))
#개요 확인
print(df.info())


#sklearn에서 제공하는 boston 주택 가격 데이터 가져오기
import numpy as np
from pandas import Series, DataFrame
import pandas as pd

#sklearn에서 데이터를 사용하기 위한 import
from sklearn import datasets

#boston 데이터 셋을 가져오기
boston = datasets.load_boston()

#자료형 확인
print(type(boston))

#데이터 확인
print(type(boston.keys)) #키의 자료형 확인
print(boston.keys())
#실제 데이터의 자료형을 확인
print(type(boston.data))
#DataFrame으로 생성가능한지 확인 - shape 확인
print(boston.data.shape)
#DataFrame으로 변환 - 컬럼이름을 확인해서 컬럼 이름 부여
#가져온 데이터 셋이 ndarray 인 경우 데이터를 파악하기가
#어려울 수 있어서 컬럼이름을 부여한 DataFrame으로 가지고 있는것이
#데이터 파악이 용이합니다.
#머신러닝에 적용할 때는 df.values 로 다시 ndarray로 만들면 됩니다.
df = DataFrame(boston.data,
   columns=['CRIM','INDUS','NOX','RM','LSTAT'
            ,'B', 'PTRATIO','ZN','CHAS',
            'AGE','RAD','DIS','TAX'])
print(df.info())

#data/data_fwf.txt 파일의 내용을 가지고 DataFrame 만들기
#텍스트를 한번에 읽은 후 슬라이싱을 이용해서 만들기도 합니다.
import os
print(os.getcwd())

fwf = pd.read_fwf('./data/data_fwf.txt',
                      width=(10,2,5),
                      names=('날짜','종목이름','종가'),
                      encoding='utf-8')
print(fwf)

#item.csv 파일을 읽어서 DataFrame 만들기
item = pd.read_csv('./data/item.csv')
print(item.head())
print(item.info())

#good.csv 파일을 읽어서 DataFrame 만들기
good = pd.read_csv('./data/good.csv'
                   ,header=None
                   ,names=['제품명','수량', '가격'])
print(good.head())
print(good.info())

#good.csv 파일의 내용을 2개씩 읽어오기
goodchunk = pd.read_csv('./data/good.csv', 
                        chunksize=2, 
                        header=None)

for two in goodchunk:
    print(two)

#문자열이 작은 따옴표로 묶여 있는 경우
fruits = pd.read_csv('./data/fruit.csv', 
                       header=None,
                       sep='|')
print(fruits)

#줄단위로 읽어서 DataFrame 만들기
import csv
lines = list(csv.reader(open('./data/fruit.csv')
    ,delimiter='|'))
print(lines)

fruits = DataFrame(lines, 
                   columns=['이름','수량','가격'])
print(fruits)

#파일에 저장
fruits.to_csv('fruits.csv')

#엑셀 파일 읽고 쓰기
excel = pd.read_excel('./data/excel.xlsx',
                      sheet_name='Sheet1')
print(excel)

writer = pd.ExcelWriter('excel.xlsx')
excel.to_excel(writer, sheet_name='연습')
writer.save()

#pandas 의 read_html 함수 도움말
help(pd.read_html)

li = pd.read_html(
   'https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D',
   thousands=',')
for df in li:
    print(df.head())
    
print(li[0])

#json 데이터 읽기
movies = pd.read_json(
    'http://swiftapi.rubypaper.co.kr:2029/hoppin/movies?version=1&page=1&count=20&genreId=&order=releasedateasc')
print(movies)
print(movies['hoppin'])
print(movies['hoppin']['movies'])
print(movies['hoppin']['movies']['movie'])
for temp in movies['hoppin']['movies']['movie']:
    print(temp['title'])

#sqlite3 의 데이터 가져오기
import pandas as pd
from sqlalchemy import create_engine 

#연결 객체 생성
con = create_engine('sqlite:///data/sample.db')

#sql을 실행해서 DataFrame 만들기
pl = pd.read_sql('select * from pl', con)
print(pl)
   
#oracle에서 데이터를 가져와서 DataFrame 만들기
#cx_Oracle 이라는 패키지를 설치
import pandas as pd
from sqlalchemy import create_engine 
    
#연결 객체 생성
con = create_engine(
    'oracle://user00:user00@211.183.6.60:1521/xe')  
dept = pd.read_sql('select * from dept', con)  
print(dept) 

#DataFrame에서의 선택
#item.csv 파일의 데이터 가져오기

import numpy as np
import pandas as pd

#item.csv 파일의 내용을 가져오기
item = pd.read_csv('./data/item.csv')
#컬럼이름: code, manufacture, name, price
print(item.head())
item.info()

#인덱스 설정
item.index = ['사과', '수박','참외','바나나','레몬', '망고']

print(item['name']) #하나의 열 선택
print(item[['name', 'price']]) #여러 개 열 선택

#행선택
print(item.loc['사과']) #인덱스로 접근
print(item.iloc[2]) #행의 위치로 접근

print(item.loc[['사과', '망고']]) #인덱스로 접근
print(item.iloc[[2, 4]]) #행의 위치로 접근

print(item.loc['사과':'망고']) #인덱스로 접근
print(item.iloc[0:5]) #행의 위치로 접근

#price가 1000 이상인 데이터만 추출
print(item[item['price'] >= 1000])

#price가 1000 이나 1500 인 데이터
print(item[item['price']
    .isin([1000, 1500])])

#데이터 탐색 함수
df = pd.read_csv("./data/auto-mpg.csv")
print(df.head())

#기술 통계 정보 확인
print(df.describe()) #숫자 데이터의 통계
print(df.describe(include='all')) #문자도 포함

#카테고리 형태의 데이터의 분포 확인
print(df['origin'].value_counts())

#cyl 컬럼의 평균
print(df['cyl'].mean())

stock = pd.DataFrame({'다음':[1000, 1200, 1960]})
print(stock['다음'].diff()) #각 행의 차이
print(stock['다음'].pct_change()) #각 행의 차이의 비율

#데이터 탐색 함수
df = pd.read_csv("./data/auto-mpg.csv")
print(df.head())
#weight 와 mpg 의 상관계수 확인
#둘다 음수가 나왔고 0.6이상이므로 음의 상관관계
print(df['weight'].corr(df['mpg']))
print(df['hp'].corr(df['mpg']))   

#Series의 정렬
print(df['hp']) 
print(df['hp'].sort_values()) #오름차순 정렬   
print(df['hp'].sort_values(ascending=False)) #내림차순 정렬
    
#hp의 오름차순 그리고 값이 같으면 cyl의 오름차순 정렬
print(df.sort_values(by=['hp', 'cyl']))

#item.csv 내용 가져오기
item = pd.read_csv('./data/item.csv')
print(item)

#순위 출력
print(item.rank())
print(item.rank(method='min'))

#컬럼이름 변경
#inplace 옵션을 이용하면 호출한 원본에 적용 가능
item.rename(columns={'code':'코드'},
            inplace=True)
print(item)

#코드를 index로 설정 - 데이터에서는 제거
item.set_index('코드', inplace=True)
print(item)



