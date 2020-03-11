import numpy as np
import pandas as pd

#0이 10개이고 1이 90개 인 ndarray 생성
list1 = []
for i in range(0,10,1):
    list1.append(0)
    
list2 = []
for i in range(0,90,1):
    list2.append(1)
    
#2개의 list를 가지고 하나의 array 생성
target = np.array(list1 + list2)
print(target)

#분류 알고리즘에 위의 데이터를 이용하는 경우
#0:10% 1:90%

#분류 알고리즘
from sklearn.ensemble import RandomForestClassifier
#데이터의 비율이 현저하게 다르기 때문에 가중치 설정
weights = {0:0.9, 1:0.1}
rfc = RandomForestClassifier(class_weight=weights)
print(rfc)
#가중치를 직접 설정하지 않고 분류기에게 판단하도록 해주는 옵션
rfc = RandomForestClassifier(class_weight='balanced')
print(rfc)

#샘플링 비율 조정
#np.where는 array에서 조건에 맞는 데이터만 추출
#np.where(target==0) - 
#target 행렬에서 값이 0인 데이터의 행번호를 리턴
#(행번호행렬, 자료형)으로 결과를 리턴
#행번호행렬만 가져오기 위해서 [0]을 추가
class0 = np.where(target==0)[0]
class1 = np.where(target==1)[0]
print(len(class0))
print(len(class1))

#target 이 1인 데이터에서 target이 0인 데이터만큼 다운 샘플링을 해서
#새로운 데이터 셋을 생성
#class1에서 class0 의 데이터 개수만큼 비복원 추출(나온것은 제거)
downsample = np.random.choice(
        class1, size=len(class0), replace=False)
result = np.hstack((target[class0], target[downsample]))
print(result)

#표준화
#student.csv 파일의 내용을 가져오기
#index로 이름을 설정
import os
print(os.getcwd())

data = pd.read_csv('./data/student.csv', index_col='이름',
                   encoding='cp949')
print(data)

import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

#그래프에 한글을 출력하기 위한 설정
#매킨토시의 경우
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
#윈도우의 경우
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
    
#인덱스를 기준으로 해서 막대 그래프 그리기
data.plot(kind='bar')

#표준값 작업
#각 과목의 평균과 표준편차 구하기
kormean, korstd = data['국어'].mean(), data['국어'].std()
engmean, engstd = data['영어'].mean(), data['영어'].std()
matmean, matstd = data['수학'].mean(), data['수학'].std()

#표준값 구하기 - (자신의 값-평균)/표준편차
#0.0이면 중간
#1.0이면 상하위 15%
#2.0이면 상하위 1.1%
data['국어표준값'] = (data['국어']-kormean)/korstd
data['영어표준값'] = (data['영어']-engmean)/engstd
data['수학표준값'] = (data['수학']-matmean)/matstd
print(data[['국어표준값', '영어표준값', '수학표준값']])

#표준값은 비교가 가능하기는 하지만 사람이 알아보기 불편
#표준값 * 10 + 50을 해서 편차값을 만들어서 보고서를 만듬
data['국어편차값'] = data['국어표준값'] * 10 + 50
data['영어편차값'] = data['영어표준값'] * 10 + 50
data['수학편차값'] = data['수학표준값'] * 10 + 50

data[['국어편차값', '영어편차값','수학편차값']].plot(kind='bar')

#최대값으로 나누어서 값을 저장 - 정규화
#자신의값-최소값/최대값-최소값으로 하기도 함
data['국어정규화1'] = data['국어'] / data['국어'].max()
data['국어정규화2'] = (data['국어']-data['국어'].min()) / (data['국어'].max()-data['국어'].min())

##sklearn 을 이용한 scailing
from sklearn import preprocessing

#StandardScaler - 평균은 0 표준편차는 1이 되도록 표준화 
scaler = preprocessing.StandardScaler()
#국어 점수만 이용하는 경우 data['국어'] 가 아니고 data[['국어']]
#머신러닝의 데이터들은 행렬을 이용하는데 data['국어']하게되면
#컬럼이름이 1개라서 하나의 열로 리턴되서 1차원 데이터가 됨
#data[['국어']] 하게되면 list를 대입했기 때문에 DataFrame으로 리턴
result = scaler.fit_transform(data[['국어']].values) 
print(result) #표준값 구한 것
print(np.mean(result)) 
print(np.std(result))

#이차원 행렬을 생성
matrix = data[['국어','영어']].values
print(matrix)

matrix = np.array([[30,20], [10, 30], [30,40]])
print(matrix)

from sklearn import preprocessing

#정규화 객체 생성 - 유클리디안 거리를 사용
norm = preprocessing.Normalizer(norm='l2')
print(norm.transform(matrix))
#합을 가지고 나누는 방식
norm = preprocessing.Normalizer(norm='l1')
print(norm.transform(matrix))

#큰값을 가지고 나누는 방식
norm = preprocessing.Normalizer(norm='max')
print(norm.transform(matrix))

matrix = np.array([[30,20], [10, 30], [30,40]])
print(matrix)

#다항과 교차항을 만들어주는 객체를 생성
#degree=2 : 제곱한 것 까지 생성
polynomial = preprocessing.PolynomialFeatures(degree=2,
                                              include_bias=False)
result = polynomial.fit_transform(matrix)
print(result)

polynomial = preprocessing.PolynomialFeatures(degree=3,
                                              include_bias=False)
result = polynomial.fit_transform(matrix)
print(result)

#함수 적용하기
matrix = np.array([[100, 200], [300,150]])
print(matrix)

#100을 결합하기
def intconvert(x):
    return x + 100

transformer = preprocessing.FunctionTransformer(intconvert)
result = transformer.transform(matrix)
print(result)


print(data['국어'])
print(data['국어'].apply(intconvert))

import numpy as np
import pandas as pd

#array를 입력받아서 z 점수(평균의 표준편차 3배 범위) 
#밖에 있는 데이터를 리턴해주는 함수

def z_score_outlier(ar):
    threshold = 3
    #평균 가져오기
    meandata = np.mean(ar)
    stdevdata = np.std(ar)
    z_scores = [(y-meandata) / stdevdata for y in ar]
    return np.where(np.abs(z_scores) > threshold)

features = np.array([[10,30, 13,-200000, 4, 12,10,30, 13,11, 4, 12,10,30, 13,10, 4, 12],
                     [2, 9, 5, 4, 2,200000,10,30, 13,20, 4, 12,10,30, 13,20, 4, 12]])

result = z_score_outlier(features)
print(result)

#z score 보정 - 범위를 3.5배로 늘리고 표준편차 0.6875를 곱해줍니다.
def modify_z_score_outlier(ar):
    threshold = 3.5
    #평균 가져오기
    meandata = np.mean(ar)
    stdevdata = np.std(ar)
    z_scores = [0.6875*(y-meandata) / stdevdata for y in ar]
    return np.where(np.abs(z_scores) > threshold)

features = np.array([[10,30, 13,-20, 4, 12,10,30, 13,11, 4, 12,10,30, 13,10, 4, 12],
                     [2, 9, 5, 4, 2,200000,10,30, 13,20, 4, 12,10,30, 13,20, 4, 12]])

result = modify_z_score_outlier(features)
print(result)

#IQR 이용 : 3사분위수-1사분위의 +- 1.5 배이상 차이나면 이상치로 간주
def iqr_outlier(ar):
    #25%와 75% 값 찾기
    q1, q3 = np.percentile(ar, [25, 75])
    print(q1, q3)
    #iqr 값 찾기
    iqr = q3 - q1
    #25% 값과 1.5 iqr보다 작은 값 찾기
    lower = q1 - (iqr * 1.5)
    upper = q3 + (iqr * 1.5)
    return np.where((ar > upper) | (ar<lower))

features = np.array([[10,30, 13,-20, 4, 12,10,30, 13,11, 4, 12,10,30, 13,10, 4, 12],
                     [2, 9, 5, 4, 2,200000,10,30, 13,20, 4, 12,10,30, 13,20, 4, 12]])

result = iqr_outlier(features)
print(result)

house = pd.DataFrame()
house['price'] = [100000, 200000, 150000, 10000000]
house['rooms'] = [1, 3, 2, 100]
house['square'] = [11, 23, 16, 1200]
print(house)

#이상한 데이터 제거 : 방이 5개 이상 제거
print(house[house['rooms'] < 6])
#이상한 데이터를 별도로 표시
#6보다 작으면 0 아니면 1을 대입
house['outlier'] = np.where(house['rooms'] < 6, 0, 1)
print(house)

#값의 범위 줄이기 - np.log는 자연로그를 계산
house['log'] = [np.log(x) for x in house['rooms']]
print(house)

#문자 데이터를 pandas의 시계열 데이터로 만들기
df = pd.read_csv('./data/stock-data.csv')
print(df)
#자료형 확인
print(df.info())
#Date 컬럼의 값을 시계열로 변경해서 추가
df['newDate'] = pd.to_datetime(df['Date'])
print(df.info())

#위와 같은 데이터프레임에서는
#날짜를 index로 설정하는 경우가 많습니다.
df.set_index('newDate', inplace=True)
df.drop('Date', axis=1, inplace=True)
print(df.head())

#일정한 간격을 갖는 날짜 만들기
dates = ['2017-03-01', '2017-06-01', '2019-12-01']
#날짜로 변경
pddates = pd.to_datetime(dates)
print(pddates)

#Period로 변환
pdperiod = pddates.to_period(freq='D')
print(pdperiod)

pdperiod = pddates.to_period(freq='M')
print(pdperiod)

pdperiod = pddates.to_period(freq='Q')
print(pdperiod)

pdperiod = pddates.to_period(freq='A')
print(pdperiod)

#일정한 간격을 가진 날짜 데이터 생성
ts_ms = pd.date_range(start='2018-01-01',
                      end=None,
                      periods=10,
                      freq = 'd')
print(ts_ms)

#문자 데이터를 pandas의 시계열 데이터로 만들기
df = pd.read_csv('./data/stock-data.csv')
print(df)
#자료형 확인
print(df.info())
#Date 컬럼의 값을 시계열로 변경해서 추가
df['newDate'] = pd.to_datetime(df['Date'])
print(df.info())

df['year'] = df['newDate'].dt.year
print(df['year'])

#python의 날짜 패키지 
from datetime import datetime

dates = [datetime(2017,1,1),
         datetime(2017,1,4),
         datetime(2017,1,7)]
ts = pd.Series(
        np.random.randn(3), index=dates)
print(ts)

print(ts.shift(-1))

#일정한 간격으로 집계
ran = pd.date_range('11/3/2020',
                    periods=20, freq='T')
print(ran)

ts = pd.Series(np.arange(20), index=ran)
print(ts)

#5분 단위로 합계
print(ts.resample('7T').mean())

#단순이동평균과 지수이동평균

#월 단위로 12개의 시간을 생성
ts = pd.date_range('2020/01/01', periods=12, freq='MS')
df = pd.DataFrame(index=ts)
print(df)

#새로운 컬럼 추가
df['data'] = [10,20,30,40,50,60,70,80,90,100,110,120]
print(df)

#단순이동평균 - 개수만 설정해서 평균을 구하는 것
print(df.rolling(window=3).mean())









