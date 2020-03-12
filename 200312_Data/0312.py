import numpy as np
import pandas as pd

#2020년 1월 1일 부터 월 단위로 5개의 데이터를 생성
timeindex = pd.date_range('01/01/2020', periods=5, freq='M')

df = pd.DataFrame(index=timeindex)

df["price"] = [10,20,30,40,50]

print(df)

#span을 2로 설정해서 지수이동평균 구하기
print(df.ewm(span=2).mean())


#2020년 1월 1일 부터 월 단위로 5개의 데이터를 생성
timeindex = pd.date_range('01/01/2020', periods=12, freq='M')

df = pd.DataFrame(index=timeindex)

#누락된 데이터(결측치 - None, null, np.nan) 만들기
df["price"] = [10,20,np.NaN,40,50,60,70,80,90,np.NaN,110,120]

#선형으로 누락된 값 채우기
print(df.interpolate())

df["price"] = [100,400,np.NaN,1600,2500,3600,
               4900,6400,8100,np.NaN,12100,14400]

#비선형으로 누락된 값 채우기
print(df.interpolate(method='quadratic'))

#seaborn 패키지에 존재하는 titanic 데이터 가져오기
#인터넷에서 가져오기 때문에 인터넷이 안되면 안됨
#seaborn 패키지: 샘플 데이터 셋과 matplotlib보다 시각적인 효과가
#뛰어난 그래프를 만들어주는 패키지
#numpy, pandas, matplotlib, seaborn, sklearn(전처리, 머신러닝)
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.info()

#2개의 컬럼을 추출해서 새로운 DataFrame 만들기
#age, fare
df = titanic[['age','fare']]
df.info()

#행전체의 age 와 fare 열 가져오기
df = titanic.loc[:, ['age','fare']]
df.info()

def add_10(x):
    return x+10
#데이터프레임에 함수 적용 - 열 단위로 적용
result = df.apply(add_10)
print(result.head())
print(result.info())

#행단위 적용
result = df.apply(add_10, axis=1)
print(result.head())
print(result.info())

#stock price.xlsx 파일과 stock valuation.xlsx 파일 읽기
price = pd.read_excel('./data/stock price.xlsx')
valuation = pd.read_excel('./data/stock valuation.xlsx')
print(price.info())
print(valuation.info())

#2개의 DataFrame을 id를 기준으로 합치기
#양쪽 모두에 존재하는 데이터만 조인에 참여 - Inner Join
merge_inner = pd.merge(price, valuation)
print(merge_inner)
print(merge_inner.info())

#어느 한쪽에만 존재하는 데이터도 join에 참여 - outer join
merge_outer = pd.merge(price, valuation, how='outer', on='id')
print(merge_outer)

#파일의 내용을 읽을 때 하나의 컬럼을 인덱스로 설정 
price = pd.read_excel('./data/stock price.xlsx', index_col='id')
valuation = pd.read_excel('./data/stock valuation.xlsx', 
                          index_col='id')
print(price.info())
print(valuation.info())
#인덱스를 이용해서 join - price의 모든 데이터는 join에 참여
#valuation에서는 참여하지 않는 데이터도 있을 수 없음
stock_join = price.join(valuation)
print(stock_join)

#concat - 열 행 방향으로 DataFrame을 합쳐주는 함수
df1 = pd.DataFrame({'a':['a0','a1','a2']}, index=[1,2,3])
df2 = pd.DataFrame({'a':['a2','a3','a4'],
                    'b':['b2','b3','b4']}, index=[2,3,4])
print(df1)
print(df2)

#위아래로 합치기
print(pd.concat([df1, df2]))

#좌우로 합치기 - 기본이 outer라서 한쪽에만 존재하는 것도 나옴
print(pd.concat([df1, df2], axis=1))

#한쪽에만 존재하는 데이터 제거
print(pd.concat([df1, df2], axis=1, join='inner'))

#행방향으로 무조건 합치기
print(df1.append(df2))

#인덱스를 가지고 합치는데 호출하는 쪽의 데이터를 우선 적용
print(df1.combine_first(df2))


import seaborn as sns

#titanic 데이터 가져오기
titanic = sns.load_dataset('titanic')
titanic.info()

#class 별로 그룹화
grouped = titanic.groupby('class')
print(grouped)

#그룹화된 데이터에 접근
for key, data in grouped:
    print(key)
    print(data.head(2))
    
#Third에 해당하는 그룹의 데이터만 가져오기
third = grouped.get_group('Third')
print(third['class'])

#집계함수 적용 - 그룹별 평균 구하기
print(grouped.mean())

#2개의 특성으로 그룹화해서 집계
grouped = titanic.groupby(['class', 'sex'])
print(grouped.mean())

#그룹화 해서 원하는 함수를 적용
def func(x):
    return x.max() - x.min()

grouped = titanic.groupby(['class'])

print(grouped.agg(func))

#여러 개의 함수를 적용
print(grouped.agg(['max', 'min']))

#각 그룹별 데이터 개수 확인
for key, data in grouped:
    print(key, len(data))

#데이터가 200개 안되는 그룹은 제거
    
#데이터의 개수가 200이상인 여부를 알려주는 함수
def over200(x):
    return len(x) >= 200

#grouped_filter = grouped.filter(over200)
    
#위의 내용을 람다함수로 변환
#파이썬에서의 람다는 이름없는 한 줄 짜리 함수 
#필터링이나 mapping(apply) 메소드에서 람다를 많이 사용
grouped_filter = grouped.filter(lambda x:len(x)>200)
print(grouped_filter['class'])

#age 열의 평균이 30이 안되는 그룹을 제거
for key, data in grouped:
    print(key, data['age'].mean())
    
grouped_filter = grouped.filter(
        lambda x:x['age'].mean()>=30)
print(grouped_filter['class'])    
    

#그룹화를 할 때 2개 이상의 컬럼 이름을 대입하면 멀티인덱스
grouped = titanic.groupby(['class', 'sex'])
gdf = grouped.mean()
print(gdf)

#행단위로 데이터 접근
print(gdf.loc['Third'])

#Third 의 male 만 가져오기
print(gdf.loc[('Third', 'male')])

#xs 인덱서 사용
print(gdf.xs('male', level='sex'))
    
import numpy as np
import pandas as pd
import seaborn as sns;

#seaborn에 존재하는 titanic 데이터 가져오기
titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.info())
    
#age, sex, class, fare, survived 컬럼만 추출해서
#새로운 데이터프레임 만들기
df = titanic[['age', 'sex','class','fare','survived']]
print(df)

df = titanic.loc[:, ['age', 'sex','class','fare','survived']]
print(df)
    
#class 별로 성별로 구분해서 age의 평균 구하기

pivot1 = pd.pivot_table(df, index=['class'], columns=['sex'],
                        values=['age'], aggfunc='mean')
print(pivot1)
    
pivot1 = pd.pivot_table(df, index=['class'], columns=['sex'],
                        values=['age'], aggfunc=['mean', 'sum'])
print(pivot1)

#인덱스로 class 와 sex를 설정
#열은 survived
#데이터는 age, fare
#집계함수는 mean 과 sum 적용
pivot1 = pd.pivot_table(df, index=['class', 'sex'],
                        columns=['survived'],
                        values=['age', 'fare'], 
                        aggfunc=['mean', 'sum'])
print(pivot1)
#첫번째 인덱스(class)가 First 인 데이터 가져오기
print(pivot1.xs('First'))

#First 이고 male 인 데이터 가져오기
print(pivot1.xs(('First', 'male'), level=['class','sex']))

#mean 열의 데이터만 가져오기
print(pivot1.xs('mean', axis=1))

''' 
    서울시 구별 CCTV 와 인구수 시각화 
'''
import pandas as pd
#1.cctv.xlsx 파일과 pop.txt 파일의 내용 읽기

cctv = pd.read_excel('./data/cctv.xlsx')
print(cctv.head())
print()
print(cctv.info())

#skiprows=2 2줄 건너뛰고 읽기
#delimiter= '\t' 구분자는 탭
#thousands=',' 천단위 구분기호는 ,
pop = pd.read_csv('./data/pop.txt', skiprows=2,
                  delimiter='\t', thousands=',')
print(pop.head())
print()
print(pop.info())

#컬럼이름 수정하고 구이름을 동일한 형태로 만들기
#inplace=True 가 설정되면 현재 데이터프레임에 적용하고
#이 옵션이 없으면 현재 데이터프레임을 복사해서 작업하고
#return을 해줍니다.
cctv.rename(columns={cctv.columns[0]:'구별'}, 
                     inplace=True)
pop.rename(columns={pop.columns[1]:'구별'}, 
                     inplace=True)
#cctv 의 구별 데이터에서 공백을 전부 제거하기
gu = []
for x in cctv['구별']:
    gu.append(x.replace(' ', ''))
cctv['구별'] = gu

print(cctv['구별'])

#pop에서 필요한 행과 열만 가져오기
#pop에서 기간, 구별, 계, 남자, 여자 열만 추출
pop = pop[['기간','구별','계','남자','여자']]

#0번 행을 제거
pop.drop([0], inplace=True)

#여성비율이라는 새로운 컬럼을 추가 - 여자/계 * 100
pop['여성비율'] = pop['여자']/pop['계'] * 100

print(pop)

#cctv 와 pop을 합치기 - 기준은 구별
df = pd.merge(cctv, pop, on='구별')
print(df)

#합쳐진 데이터프레임에서 불필요한 컬럼 제거
#2011년 이전, 2012년, 2013년, 2014년, 2015년, 2016년, 2017년, 기간
df.drop(['2011년 이전', '2012년', '2013년',
         '2014년', '2015년', '2016년','2017년', '기간'], axis=1, inplace=True)
print(df)

#구별 컬럼을 인덱스로 설정
df.set_index('구별', inplace=True)
print(df)

#그래프 그리기 위한 패키지
import matplotlib.pyplot as plt

#그래프에서 한글 처리를 위한 패키지
from matplotlib import font_manager, rc
import platform

#운영체제를 확인해서 글꼴 설정
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(
            fname='c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', famaly='AppleGothic')

#cctv 개수를 가지고 막대 그래프 그리기
df['소계'].plot(kind='bar', figsize=(10,10))
plt.show()

#cctv 개수를 가지고 막대 그래프 그리기 - 정렬
df['소계'].sort_values().plot(kind='bar', figsize=(10,10))
plt.show()

#인구수(계)와 cctv 개수(소계)를 가지고 산포도 그리기
plt.figure(figsize=(8,8))
plt.scatter(df['계'], df['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('cctv 개수')
plt.grid()
plt.show()

#계와 소계의 데이터를 가지고 다항식 구하기
import numpy as np
fp1 = np.polyfit(df['계'], df['소계'], 1)
f1 = np.poly1d(fp1)
print(f1)

#선그래프 그리기
#100000 부터 700000까지를 100개로 분할 배열 생성
fx = np.linspace(100000, 700000, 100)
plt.figure(figsize=(8,8))
plt.scatter(df['계'], df['소계'], s = 50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('cctv 개수')
plt.grid()
plt.show()

#잔차를 색상으로 표시하고 지역 이름을 점위에 출력
#잔차 계산
df['잔차'] = np.abs(df['소계'] - f1(df['계']))
plt.figure(figsize=(14,12))
plt.scatter(df['계'], df['소계'],c=df['잔차'], s = 50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')

#그래프에 텍스트 출력하기
for n in range(25):
    plt.text(df['계'][n]*1.02, df['소계'][n]*0.98,
             df.index[n], fontsize=12)

plt.xlabel('인구수')
plt.ylabel('cctv 개수')
plt.colorbar()
plt.grid()
plt.show()

#stack 과 unstack

#멀티 인덱스 만들기
#튜플의 list를 이용해서 멀티 인덱스 만들기
mul_index = pd.MultiIndex.from_tuples(
        [('cust_1','2015'),('cust_1','2016'),
         ('cust_2','2015'),('cust_2','2016')])
    
#데이터 프레임 만들기
data = pd.DataFrame(data=np.arange(16).reshape(4,4),
            index = mul_index,
            columns=['prd_1', 'prd_2','prd_3', 'prd_4'])
print(data)

#컬럼들을 인덱스로 설정 - stack
#모든 열을 세로 방향으로 세워서 하나의 열로 만듭니다.
#index는 1개의 level이 더 많아 집니다.
data_stacked = data.stack()
print(data_stacked)

#unstack은 데이터를 가로 방향으로 늘어뜨리는 것
#level 옵션을 이용해서 원하는 만큼만 열로 만들 수 있습니다.
#지금같은 경우는 index가 3가지 이므로 0,1,2 가능
print(data_stacked.unstack(level=0))

print(data_stacked.unstack(level=2))
print(data_stacked.unstack(level=2).unstack(level=1))


#2개의 컬럼을 합쳐서 1개로 만들기
#남겨두고자 하는 컬럼의 list를 id_vars에 대입하면
#나머지 컬럼을 합쳐서 컬럼의 이름은 variable
#값은 value에 설정합니다.
print(data)
print(pd.melt(
        data, id_vars=['prd_3', 'prd_4']))

#도수분포표 - crosstab
data = pd.DataFrame({
        'id':['id1','id1','id1','id2','id2','id2'],
        'fac_1':['a','a','a','b','b','b'],
        'fac_2':['c','c','c','c','d','d']})

print(pd.crosstab(data['fac_1'], data['fac_2']))

#비율로 출력하기
print(pd.crosstab(data['fac_1'], data['fac_2'],
                  normalize=True))







