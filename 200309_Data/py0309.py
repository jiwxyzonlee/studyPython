# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:10:35 2020

@author: admin
"""

import os

os.getcwd()
os.chdir("C:/Users/admin")

import pandas as pd

pop = pd.read_excel('./data/시도_별_이동자수.xlsx')
#print(pop.head())


# na(None, numpy.NaN ...) 값을 데이터로 채우기
# 파이썬의 분석 라이브러리의 수정하는 메소드들은 대부분 수정해서 복사본을 리턴함
# 원본에 반영할 때는 다시 대입하거나 
# inplace 옵션이 있으면 이 옵션에 True를 대입
pop = pop.fillna(method = 'ffill')
#print(pop.head())


# 전출지별은 서울특별시이고 전입지는 서울특별시가 아닌 데이터만 추출하기 위한 조건 만들기
mask = (pop['전출지별'] == '서울특별시') & (pop['전입지별'] != '서울특별시')
#print(pop[mask])


# 전출지별 열을 제거
df_seoul = pop[mask].drop(['전출지별'], axis = 1)
#print(df_seoul)

# 전입지별 컬럼이름을 전입지로 수정
# inplace 옵션을 이용해서 원본에 반영
df_seoul.rename({'전입지별':'전입지'}, axis = 1, inplace=True)
#print(df_seoul.head())

# 인덱스를 기존 컬럼으로 변경 후 컬럼 제거
df_seoul.set_index('전입지', inplace = True)
#print(df_seoul.head())


# 전라남도로 전출간 인원에 대한 선 그래프 그리기
sr_one = df_seoul.loc['전라남도']

'''
# 1970, 1971 제거
sr_one.drop(['1970', '1971'], inplace = True)

# 광역시는 80년부터 생겨서 80년 이전 값이 NA이므로 먼저 제거해줘야 

'''

import matplotlib.pyplot as plt
#plt.plot(sr_one.index, sr_one.values)

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
import platform

#매킨토시의 경우
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')

#윈도우의 경우
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

# 스타일 설정
plt.style.use('ggplot')

# 이미지 사이즈 설정 - 단위는 인치
plt.figure(figsize = (14, 5))

# 눈금 조정
plt.xticks(size = 10, rotation = 'vertical') # rotation은 회전 방향

# 그래프 그리기
plt.plot(sr_one.index, sr_one.values, marker = 'o', markersize = 10)

# 그래프 제목
plt.title('서울-전라남도 이동', size = 30)
# 축 제목
plt.xlabel('기간', size = 20)
plt.ylabel('인구 수', size = 20)

# 범례
plt.legend(labels = ['서울 -> 전라남도'], loc = 'best', fontsize = 15)

# 그래프 위에 글자 작성
plt.annotate('인구이동 감소'
             , xy = (40, 300)
             , rotation = -11
             , va = 'baseline'
             , ha = 'center'
             , fontsize = '15')

plt.show()


# 기존데이터에서 전라남도에서 서울로 이동한 인구수 찾
mask = (pop['전출지별'] == '전라남도') & (pop['전입지별'] != '전라남도')
df_jeo = pop[mask]
#print(df_jeo.head())

# 전출지별 컬럼 제거
df_jeo = df_jeo.drop(['전출지별'], axis = 1)

# 컬럼이름 변경
df_jeo.rename({'전입지별':'전입지'}, axis = 1, inplace = True)

# 인덱스 설정
df_jeo.set_index('전입지', inplace = True)

# 서울로 이동한 데이터만 가져오기
sr_two = df_jeo.loc['서울특별시']
print(sr_two.head())

# 여러 개의 그래프를 그리기 위해 그리기 객체를 돌려 받기
fig = plt.figure(figsize = (10, 10))

# 2행 1열에서 1번
ax1 = fig.add_subplot(2, 1, 1)

# 2행 1열에서 2
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(sr_one
         , marker = 'o'
         , markersize = 10
         , color = 'orange'
         , linewidth = 2
         , label = '서울 -> 전라남도')

# ax1으로 고칠시 하나에 두 개의 그래프가 그려짐
ax1.plot(sr_two
         , marker = 'o'
         , markersize = 10
         , color = 'green'
         , linewidth = 2
         , label = '전라남도 -> 서울')
"""
ax2.plot(sr_two
         , marker = 'o'
         , markersize = 10
         , color = 'green'
         , linewidth = 2
         , label = '전라남도 -> 서울')
"""

# y축 눈금범위 설
ax1.set_ylim(10000, 150000)
ax2.set_ylim(10000, 150000)

ax1.set_xticklabel(sr_one.index, rotation = 75)
ax1.set_xticklabel(sr_two.index, rotation = 75)

plt.show()


# 막대 그래프 그리기
plt.bar(sr_one.index, sr_one, width = 1, color = 'r')

# x축 레이블 변겅
plt.xticks(range(0, len(sr_one.index), 1), sr_one.index, rotation = 'vertical')

plt.show()


## 서울에서 전라남도, 경상남도, 충청남도, 경기도로 전출간 인원을 막대 그래프로 비교
# 커널 재시작
import pandas as pd

df = pd.read_excel('data/시도_별_이동자수.xlsx'
                   , header = 0
                   , fillna = 0)
print(df.head())

# NaN 값들을 이전 값으로 채우기
df = df.fillna(method = 'ffill')
print(df.head())

# 전출지별이 서울특별시이고 전입지별이 서울특별시가 아닌 
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')

# mask의 결과가 True인 것만 추출
df_seoul = df[mask]
print(df_seoul.head())

# 불필요한 열 제거
df_seoul.drop(['전출지별'], axis = 1, inplace = True)
print(df_seoul.head())

# 불필요한 행 제거 - 인덱스 설정을 안 한 경우 일련번호를 이용하여 제거
#df_seoul.drop([0, 1, 2, 3, 4, 5], inplace = True)
#print(df_seoul.head())

# 기존 컬럼에서 인덱스 설정
df_seoul.set_index(['전입지별'], inplace = True)
print(df_seoul.head())

# 행단위로 골라내기 - 인덱스를 이용
sr = df_seoul.loc[['경기도', '경상남도', '전라남도', '충청남도']]
print(sr)

# 행과 열을 치환
sr = sr.T
print(sr)


# 데이터 모임에 동일한 함수를 적용한 후 결과 만들기
# sr.index에 int라는 함수를 각 요소마다 대입하여 실행한 후
# 해당 결과를 가지고 다시 데이터 모임을 생성
sr.index = sr.index.map(int)

# 그래프 그리기
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
#plt.plot(sr_one.index, sr_one.values)

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
import platform

#매킨토시의 경우
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')

#윈도우의 경우
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

plt.figure(figsize = (15, 6))
plt.bar(pd.RangeIndex(0, len(sr.index), 1)
    , sr['경기도'], color = 'orange', width = 0.25, label = '경기도')
plt.bar(pd.RangeIndex(0, len(sr.index), 1) + 0.25
        , sr['경상남도'], color = 'blue', width = 0.25, label = '경상남도')
plt.bar(pd.RangeIndex(0, len(sr.index), 1) + 0.5
        , sr['전라남도'], color = 'green', width = 0.25, label = '전라남도')
plt.bar(pd.RangeIndex(0, len(sr.index), 1) + 0.75
        , sr['충청남도'], color = 'red', width = 0.25, label = '충청남도')
# 순서 바꾸면 경기도 막대그래프 그림에 전라남도 그래프 그림이 겹쳐져서 안 보이게 됨
# width 조절 필요

# 범례 표시
plt.legend()

plt.title('서울에서의 인구이동')
plt.show()


# lovefruits.csv 파일의 내용 읽어오기
df = pd.read_csv('./data/lovefruits.csv', encoding = 'cp949')
print(df)

# 막대 그래프를 이용해서 데이터 개수 출력
# 데이터 개수 가져오기
data = df['선호과일'].value_counts(sort = False)
print(data)
"""
체리      8
복숭아    11
바나나     3
포도      5
사과      4
Name: 선호과일, dtype: int64
"""

plt.bar(range(0, len(data), 1), data)
plt.xticks(range(0, len(data), 1), data.index);
plt.title('과일 선호도 조사')
plt.show()

# 히스토그램을 이용해서 데이터 개수 출력
plt.hist(df['선호과일'])
plt.show()


# 히스토그램은 bins 옵션을 이용해서 구간의 개수를 설정해서 그릴 수 있음
# 연속형 데이터의 히스토그램은 구간 설정 필요
df = pd.read_csv('./data/student.csv', encoding = 'cp949')
print(df)
plt.hist(df['수학'], bins = 3)
plt.show()


# 산포도 그리기
# korea.csv 파일의 내용을 읽어서 학생별 점수를 산포도로 출력

# 1. 데이터 읽어오기
# 구분자는 ',' 한글이 포함되어 있고 첫번째 행이 컬럼이름
df = pd.read_csv('./data/korea.csv', encoding = 'cp949')

# 2. 읽어온 데이터 확인
print(df.head())
print(df.info())

plt.figure()
colormap = df.index
plt.scatter(df.index, df['점수'], marker = '2', c = colormap)
plt.xticks(range(0, len(df.index), 1)
            , df['이름'], rotation = 'vertical') # 눈금 바꾸기
plt.colorbar()

plt.show()


# 컬럼 2개의 관계를 파악하기 위한 산포도
df = pd.read_csv('./data/auto-mpg.csv')
# 한글 없으므로 인코딩 불필요

df.columns = ['mpg', 'cylinders', 'displacement'
              , 'horesepower', 'weight', 'acceleration'
              , 'model year', 'origin', 'name']

# s는 원의 크기 옵션
plt.scatter(df['weight'], df['mpg'], s = df['cylinders']*5, alpha = 0.5)
plt.title('중량과 연비의 관계')
plt.xlabel('중량', size = 20)
plt.ylabel('연비', size = 20)

#print(df.head())
plt.show()



# 원그래프 그리기
df = pd.read_csv('./data/korea.csv', encoding = 'cp949')
print(df.head())

explode = []
for i in range(0, 20, 1):
    explode.append(0)
explode[2] = 0.3

plt.figure(figsize = (15, 8))
plt.pie(df['점수']
        , labels = df['이름']
        , explode = explode
        , autopct = '%1.1f%%')
plt.title('학생별 기여도')
plt.legend()
plt.show()


# 상자 그래프 그리기
df = pd.read_csv('./data/student.csv', encoding = 'cp949')
plt.boxplot((df['국어'], df['영어'], df['수학'])
            , labels = ('국어', '영어', '수학'))
plt.show()


## 커널 재시작
# import된 모든 라이브러리 제거
# 변수도 모두 제거
import matplotlib.pyplot as plt

# 시각적인 효과가 조금 뛰어난 그래프 패키지
import seaborn as sns

# tips라는 데이터 가져오기 - 레스토랑에서의 tip과 관련된 데이터 모음
tips = sns.load_dataset('tips')
print(tips)

fig = plt.figure(figsize = (8, 6))
# 1행 2열 1번째 영역
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

sns.set_style("darkgrid")

# data에 DataFrame을 x, y에 컬럼이름을 설정
sns.regplot(x = 'total_bill', y = 'tip', data = tips, fit_reg = True, ax = ax1)
sns.regplot(x = 'total_bill', y = 'tip', data = tips, fit_reg = False, ax = ax2)

plt.show()

# 3개 컬럼의 관계 보기 - lmplot
# x, y, hue 옵션 이용
# hue에는 카테고리(범주) 데이터를 설정

fig = plt.figure(figsize = (8, 6))
sns.set_style("darkgrid")
# data에 DataFrame을 x, y에 컬럼이름을 설정
sns.lmplot(x = 'total_bill', y = 'tip', hue = 'smoker', data = tips, fit_reg = True)

plt.show()


# tip 컬럼의 분포를 확인
fig = plt.figure(figsize = (8, 6))
sns.set_style("darkgrid")
sns.distplot(tips['tip'], hist = False)
plt.show()


# heatmap (2가지로 분류해서 하나의 통계값 출력) 만들기
flights = sns.load_dataset('flights')
print(flights.head())

# pivot 테이블 만들기
pivot = flights.pivot('month', 'year', 'passengers')
print(pivot)

plt.figure(figsize = (10, 8))
# annot는 데이터를 화면에 출력할 것인지 여부
# fmt는 숫자 출력 포맷 (d를 설정 시 정수로 출력)
sns.heatmap(pivot, annot = True, fmt = 'd')
plt.show()


# tips 데이터의 모든 컬럼의 산점도를 출력
plt.figure(figsize = (10, 8))
sns.pairplot(tips)
plt.show()


