#작업 디렉토리 확인
import os
print(os.getcwd())

##경기도인구데이터.xlsx 파일과 경기도행정구역경계.json
#파일을 이용한 단계구분도 만들기
import pandas as pd
#구분 컬럼을 인덱스로 설정
df = pd.read_excel('./data/경기도인구데이터.xlsx',
                   index_col='구분')
#인덱스에 str 함수를 적용해서 문자열로 자료형을 변경
#인덱스를 숫자 자료형으로 만들면 인덱스가 행의 위치인지
#인덱스인지 혼동이 올 수 있습니다.
#loc[인덱스], iloc[행의위치]

#컬럼의 이름들도 문자로 만드는 것이 좋습니다.
#컬럼의 접근:데이터프레임[컬럼이름], 데이터프레임.컬럼이름
#컬럼의 이름이 숫자이면 데이터프레임.컬럼이름 은 사용할 수 
#없습니다.

#컬럼의 이름들을 문자열로 변경
df.columns = df.columns.map(str)

print(df.head())

##json 파일 읽기
import json
#파일의 경우는 open 함수에 파일의 경로를 대입해야 하고
#텍스트 데이터의 경우는 바로 입력하면 됩니다.
geo_data = json.load(
        open('./data/경기도행정구역경계.json',
             encoding='utf-8'))

print(geo_data)

#지도 만들기 - 기본 패키지가 아님
import folium
g_map = folium.Map(location=[37.5500, 126.9800],
                   zoom_start=9)

#단계 구분도 만들기
#threshold_scale: 색상을 구분하기 위한 숫자 리스트
#key_on: json 파일에서 각 영역의 이름을 나타내는 프로퍼티를 지정
folium.Choropleth(geo_data=geo_data,
                  data=df['2017'],
                  fill_color='YlGn',
                  fill_opacity=0.5,
                  line_opacity=0.3,
                  threshold_scale=[10000, 100000, 300000, 500000, 700000],
                  key_on='feature.properties.name').add_to(g_map)

g_map.save('g_map.html')


#pandas 패키지의 시각화
df = pd.read_csv('./data/seoul.csv')
print(df.head())
df.plot()

#수치연산 과 선형대수 그리고 ndarray라는 자료구조를 가진 패키지
import numpy as np
#Series 와 Dataframe 이라는 자료구조를 가진 패키지
import pandas as pd
#샘플 데이터와 시각화를 위한 패키지
import seaborn as sns

#titanic 데이터 가져오기
titanic = sns.load_dataset('titanic')

#데이터 탐색
print(titanic.head())
print()
titanic.info()

#NaN이 존재하는지 확인
#titanic에서 앞 쪽 10개의 데이터가 NaN을 포함하는지 확인
print(titanic.head(10).isnull())

#titanic에서 NaN을 포함한 행의 개수를 파악
print(titanic['age'].isnull().sum(axis=0))

#NaN이 300개 이상인 열을 제거
#NaN이 너무 많아서 제거
titanic.dropna(thresh=300, axis=1, inplace=True)
print(titanic.info())

#age 열의 값이 NaN 인 행을 제거 - 아주 많지 않으면 행을 제거
titanic.dropna(subset=['age'], 
               how='any', axis=0, inplace=True)
print(titanic.info())

#데이터 다시 가져오기
titanic = sns.load_dataset('titanic')
print(titanic['embarked'][820:830])

#직접 NaN 값을 다른 값으로 대체 - 앞의 데이터로 채움
#표 형태의 데이터를 가져온 경우 셀 병합이 된 경우에 사용
titanic['embarked'].fillna(
        method='ffill', inplace=True)
print(titanic['embarked'][820:830])

#사이킷 런을 이용해서 결측치 채우기
features = np.array([[100], [200], [300], [500], [40], [np.NaN]])

#중간값으로 채우는 imputer 생성
from sklearn.impute import SimpleImputer
imputers = SimpleImputer(strategy='median')

features_imputed = imputers.fit_transform(features)
print(features_imputed)


#KNN(분류) 알고리즘을 이용한 결측치 채우기
#fancyimpute 설치를 하고 실행
#KNN을 사용하지 않고 다른 머신러닝의 분류 알고리즘을 사용해도 됩니다.
from fancyimpute import KNN
features = np.array(
        [[200,300],[300,500], [400,410], [205, np.NaN]])
features_imputed = KNN(k=5, verbose=0).fit_transform(features)
print(features_imputed)


#중복 데이터 처리
df = pd.DataFrame(
    [['차범근', '크루이프','차범근'],
     ['대한민국','네델란드','대한민국']])
df = df.T
print(df)

#중복된 데이터 확인
print(df.duplicated())

#중복된 데이터 제거
df.drop_duplicates(inplace=True)
print(df)

#auto-mpg_1.csv 파일의 내용을 가져오기
df = pd.read_csv('./data/auto-mpg_1.csv', header=None)
df.columns = ['mpg','cylinders','displacement',
              'horsepower', 'weight','acceleration',
              'model year','origin','name']
print(df.head())
print(df.info())

#origin의 경우는 생산국가
#1이면 미국 2이면 유럽 3이면 일본
#현재 데이터는 1,2,3 숫자 형태로 존재
#origin 데이터를 문자열로 치환하고 자료형을 category 로 변환
#자료형 변환은 astype('자료형')으로 가능

#문자열로 치환
df['origin'].replace({1:'미국', 2:'유럽', 3:'일본'},
  inplace=True)
print(df.head())
print(df['origin'].dtypes)

#데이터를 범주형(category)으로 변환
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

#문자열로 변환
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

print(df['horsepower'])
print(df['displacement'])

#displacement를 대형, 중형, 소형으로 새로운 컬럼 만들기

#3등분할 숫자 배열 만들기
count, bin_dividers = np.histogram(df['displacement'], bins=3)
print(bin_dividers)

#치환할 데이터 배열 만들기
bin_names = ['소형', '중형', '대형']

#치환
df['차량분류'] = pd.cut(x = df['displacement'],
                        bins=bin_dividers,
                        labels=bin_names,
                        include_lowest = True)
print(df['차량분류'])


age = np.array([[30], [40], [29], [50], [60]])
#40을 기준으로 분할 - 경계값이 다음 그룹으로 분할
print(np.digitize(age, bins=[40]))
#right를 이용하면 경계값이 아래 그룹으로 분할
print(np.digitize(age, bins=[30, 50], right=True))

#여러 개의 열로 구성된 데이터의 이산화
sample = np.array([[20,30],[40,70],[30,60],
                   [25,56],[30,20],[50,60]])
df = pd.DataFrame(sample)
print(df)

#KMeans 군집 분석을 위한 라이브러리 
from sklearn.cluster import KMeans
#군집분석 객체 생성
cluster = KMeans(3, random_state=0)
#데이터를 가지고 훈련
cluster.fit(sample)
#예측 - 군집
df['group'] = cluster.predict(sample)
print(df)

#auto-mpg_1.csv 파일의 내용을 가져오기
df = pd.read_csv('./data/auto-mpg_1.csv', header=None)
df.columns = ['mpg','cylinders','displacement',
              'horsepower', 'weight','acceleration',
              'model year','origin','name']
print(df.head())
print(df.info())

#horsepower를 저출력, 보통출력, 고출력으로 구간 분할
#범주형 목록을 생성
bin_names = ['저출력','보통출력','고출력']
#3개로 나눌 경계값을 생성
count, bin_dividers = np.histogram(df['horsepower'], bins = 3)
print(bin_dividers)

#?인 데이터를 NaN으로 치환하고 NaN 인 데이터를 제거
df['horsepower'].replace('?', np.NaN, inplace=True)
df.dropna(subset=['horsepower'], inplace=True, axis=0)

#데이터 형변환
df['horsepower'] = df['horsepower'].astype(float)

#구간분할
df['hp_bin'] = pd.cut(x=df['horsepower'],
                      bins=bin_dividers,
                      labels=bin_names,
                      include_lowest=True)
print(df['hp_bin'])

#hp_bin을 원핫인코딩 - 3개의 컬럼이 생성되고 
#컬럼의 이름은 저출력, 보통출력, 고출력이 됩니다.
#자신의 값과 일치하는 컬럼에만 1이 되고 나머지 컬럼에는 0이 대입
#저출력 보통출력 고출력
# 0      1      0
dummy = pd.get_dummies(df['hp_bin'])
print(dummy)

#사이킷 런을 이용한 원핫인코딩
from sklearn.preprocessing import LabelBinarizer

#[[0 1 0]]
one_hot = LabelBinarizer()
print(one_hot.fit_transform(df['hp_bin']))
#데이터를 정렬하기 때문에 순서를 확인
print(one_hot.classes_)

print(one_hot.inverse_transform(
        one_hot.fit_transform(df['hp_bin'])))

#여러 개의 특성을 원핫인코딩
#1개의 데이터가 여러 개의 특성을 갖는 경우 - tuple, list 등
#문장의 유사도나 상품 추천 할 때 사용
from sklearn.preprocessing import MultiLabelBinarizer
features = [('Java', 'C++'), ('Java','Python'),
            ('C#', 'R'),('Python', 'R') ]
one_hot = MultiLabelBinarizer()
print(one_hot.fit_transform(features))
print(one_hot.classes_)

#get_dummies는 하나의 특성을 하나의 컬럼으로 생성
#값의 종류가 15가지이면 15개의 컬럼을 생성
#컬럼을 1개만 만들고 0부터 일련번호 형태로 값을 설정
from sklearn.preprocessing import LabelEncoder
one_hot = LabelEncoder()
print(one_hot.fit_transform(df['hp_bin']))

#sklearn 의 인코더들은 문자열을 기준으로 정렬을 한 후
#수치를 부여 
#원하는 수치값을 부여할 수 없습니다.
#범주형 데이터에 원하는 수치값을 부여해서 인코딩할 때는 
#replace 메소드나  OrdinalEncoder 이용

#이상태에서 인코딩하면 보통 -> 우수 -> 저조 순입니다.
df = pd.DataFrame(
    {"Score":['저조','우수','보통','보통', '저조']})
print(df)

mapper = {'저조':0, '보통':1, '우수':2}

#저조:0, 보통:1, 우수:2
df['encoder'] = df['Score'].replace(mapper)
print(df)

#순서가 있는 범주형 인코딩
from sklearn.preprocessing import OrdinalEncoder


features = np.array([['대한민국', 30],
                     ['미국', 10],
                     ['뉴질랜드', 25],
                     ['캐나다', 20]])

#각 컬럼의 데이터를 정렬하고 순서대로 가중치를 부여
encoder = OrdinalEncoder()
result = encoder.fit_transform(features)
print(result)

#머신러닝 알고리즘을 이용한 누락된 값 대체
from sklearn.neighbors import KNeighborsClassifier

#훈련할 데이터
X = np.array([[0, 2.10, 1.45],
              [1, 2.10, 1.33],
              [0, 1.22, 1.27],
              [1, -0.10, -1.45]])

#NaN을 가진 데이터
X_with_nan = np.array([[np.NaN, 2.10, 1.34],
                       [np.NaN, -0.67, -0.22]])
#분류기를 생성
clf = KNeighborsClassifier(3, weights='distance')
#훈련 - 1번째 이후 데이터 전체를 가지고 0번째 데이터를 예측
trained_model = clf.fit(X[:,1:], X[:,0])
#데이터 예측
imputed_values = trained_model.predict(X_with_nan[:,1:])
print(imputed_values)







