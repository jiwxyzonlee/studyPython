#배열 자료구조(행렬 포함), 선형대수, 과학 기술 계산을 위한 패키지
import numpy as np
#Series,DataFrame(자료구조), 기술 통계, 간단한 시각화를 위한 패키지
import pandas as pd

#시각화 기본 패키지
import matplotlib.pyplot as plt

#그래프에서 한글 처리를 위한 패키지
import platform
from matplotlib import font_manager, rc

#데이터 셋과 화려한 시각화를 위한 패키지
import seaborn as sns
#데이터 전처리를 위한 패키지
#sklearn 은 데이터셋과 전처리 그리고 머신러닝을 위한 패키지
from sklearn import preprocessing

#지도 시각화(단계 구분도)를 위한 패키지
import folium

#그래프에서 한글 처리를 위한 설정
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(
        fname = 'c:/windows/fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')

#음수 사용을 위한 설정
plt.rcParams['axes.unicode_minus'] = False

#엑셀 파일의 내용을 읽기
population = pd.read_excel(
        './data/population_raw_data.xlsx', header=1)
#제대로 데이터를 읽었는지 확인
print(population.head())
population.info()

#이 엑셀 파일에서는 위와 항목이름이 같은 경우가 NA
#이전 값으로 NA를 채우기
population.fillna(method='ffill', inplace=True)
print(population.head())
population.info()

#컬럼 이름 변경
population.rename(columns={'행정구역(동읍면)별(1)':'광역시도',
                   '행정구역(동읍면)별(2)':'시도',
                   '계':'인구수'},
                   inplace=True)
population.info()

#시도가 소계인 데이터를 제외
#제외를 할 때는 drop을 이용해서 삭제를 할 수 도 있고
#필터링을 할 수 도 있습니다.

population = population[(population['시도'] != '소계')]
print(population.head())

#항목 컬럼을 구분으로 변경
population.rename(columns={'항목':'구분'}, inplace=True)

#셀의 값 변경
#구분이 총인구수 (명) -> 합계
#구분이 남자인구수 (명) -> 남자
#구분이 여자인구수 (명) -> 여자

population.loc[population['구분'] == '총인구수 (명)',
               '구분'] = '합계'
population.loc[population['구분'] == '남자인구수 (명)',
               '구분'] = '남자'
population.loc[population['구분'] == '여자인구수 (명)',
               '구분'] = '여자'
print(population['구분'].head())

#청년과 노년 층으로 새로운 컬럼을 추가
population['청년'] =  population['20 - 24세'] + population['25 - 29세'] + population['30 - 34세'] + population['35 - 39세']

population['노년'] = population['65 - 69세'] + population['70 - 74세'] + population['75 - 79세'] + population['80 - 84세'] +population['85 - 89세'] + population['90 - 94세'] +population['95 - 99세'] + population['100+']

print(population['청년'].head())
print(population['노년'].head())

#광역시도와 시도별 그리고 구분 별로 청년과 노년의 값 확인
pop = pd.pivot_table(population, 
                     index = ['광역시도', '시도'],
                     columns = '구분',
                     values = ['인구수', '청년','노년'])
print(pop.head())

#소멸비율 컬럼 - 청년층 여자 / 노년층 합계 / 2
pop['소멸비율'] = pop['청년', '여자'] / (pop['노년', '합계'] / 2)
print(pop['소멸비율'].head())

#소멸위기지역이라는 컬럼을 추가 - 소멸비율 < 1.0 여부
pop['소멸위기지역'] = pop['소멸비율'] < 1.0
print(pop['소멸위기지역'])
print(pop[pop['소멸위기지역'] == True].index.get_level_values(1))

print(pop)

#인덱스 제거
pop.reset_index(inplace=True)
print(pop.head())

#컬럼이름 만들기 - 컬럼이름이 2레벨로 되어 있어서 위아래 레벨을 합치는 작업
tmp_columns = [pop.columns.get_level_values(0)[n] + 
               pop.columns.get_level_values(1)[n] 
               for n in range(0, len(pop.columns.get_level_values(0)))]
print(tmp_columns)

pop.columns = tmp_columns
print(pop.head())

#시도이름을 확인
print(len(pop['시도'].unique()))

#시도이름 만들기
si_name = [None] * len(pop)


#광역시가 아닌 곳 중에서 구를 가지고 있는 곳의 디셔너리 만들기
tmp_gu_dict = {'수원':['장안구', '권선구', '팔달구', '영통구'], 
                       '성남':['수정구', '중원구', '분당구'], 
                       '안양':['만안구', '동안구'], 
                       '안산':['상록구', '단원구'], 
                       '고양':['덕양구', '일산동구', '일산서구'], 
                       '용인':['처인구', '기흥구', '수지구'], 
                       '청주':['상당구', '서원구', '흥덕구', '청원구'], 
                       '천안':['동남구', '서북구'], 
                       '전주':['완산구', '덕진구'], 
                       '포항':['남구', '북구'], 
                       '창원':['의창구', '성산구', '진해구', '마산합포구', '마산회원구'], 
                       '부천':['오정구', '원미구', '소사구']}

for n in pop.index:
    #광역시나 특별시 또는 자치시로 끝나지 않는
    if pop['광역시도'][n][-3:] not in ['광역시', '특별시', '자치시']:
        #중복된 지역인 고성에 대한 처리
        if pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '강원도':
            si_name[n] = '고성(강원)'
        elif pop['시도'][n][:-1] == '고성' and pop['광역시도'][n] == '경상남도':
            si_name[n] = '고성(경남)'
        else:
            si_name[n] = pop['시도'][n][:-1]
            #광역시나 특별시 자치시가 아닌데 구를 가지고 있는곳 처리
            for keys, values in tmp_gu_dict:
                if pop['시도'][n] in values:
                    if len(pop['시도'][n]) == 2:
                        si_name[n] = keys + ' ' + pop['시도'][n]
                    elif pop['시도'][n] in ['마산합포구', '마산회원구']:
                        si_name[n] = keys + ' ' + pop['시도'][n][2:-1]
                    else:
                        si_name[n] = keys + ' ' + pop['시도'][n][:-1]
    elif pop['광역시도'][n] == '세종특별자치시':
        si_name[n] = '세종'
    else:
        if len(pop['시도'][n]) == 2:
            si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n]
        else:
            si_name[n] = pop['광역시도'][n][:2] + ' ' + pop['시도'][n][:-1]
            
print(si_name)
            
#시도 이름을 pop에 새로운 컬럼으로 추가
pop['ID'] = si_name

print(pop['ID'])

#현재 상태 확인
print(pop.info())


#지도 정보를 가진 Excel 파일 읽기
draw_korea_draw = pd.read_excel('./data/draw_korea_raw.xlsx')
print(draw_korea_draw)

#컬럼이름이 일련번호로 되어 있습니다.
#stack 함수를 이용해서 컬럼이름을 인덱스로 만들기
draw_korea_raw_stacked = pd.DataFrame(draw_korea_draw.stack())
print(draw_korea_raw_stacked)

#인덱스를 초기화해서 인덱스가 컬럼이 되도록 하기
draw_korea_raw_stacked.reset_index(inplace=True)
print(draw_korea_raw_stacked)

#좌표로 사용하기 위해서 컬럼 이름 변경
draw_korea_raw_stacked.rename(columns = 
                    {'level_0':'y','level_1':'x',0:'ID'},
                    inplace=True)
print(draw_korea_raw_stacked)


#경계선을 위한 좌표 생성
BORDER_LINES = [
    [(5, 1), (5,2), (7,2), (7,3), (11,3), (11,0)], # 인천
    [(5,4), (5,5), (2,5), (2,7), (4,7), (4,9), (7,9), 
     (7,7), (9,7), (9,5), (10,5), (10,4), (5,4)], # 서울
    [(1,7), (1,8), (3,8), (3,10), (10,10), (10,7), 
     (12,7), (12,6), (11,6), (11,5), (12, 5), (12,4), 
     (11,4), (11,3)], # 경기도
    [(8,10), (8,11), (6,11), (6,12)], # 강원도
    [(12,5), (13,5), (13,4), (14,4), (14,5), (15,5), 
     (15,4), (16,4), (16,2)], # 충청북도
    [(16,4), (17,4), (17,5), (16,5), (16,6), (19,6), 
     (19,5), (20,5), (20,4), (21,4), (21,3), (19,3), (19,1)], # 전라북도
    [(13,5), (13,6), (16,6)], # 대전시
    [(13,5), (14,5)], #세종시
    [(21,2), (21,3), (22,3), (22,4), (24,4), (24,2), (21,2)], #광주
    [(20,5), (21,5), (21,6), (23,6)], #전라남도
    [(10,8), (12,8), (12,9), (14,9), (14,8), (16,8), (16,6)], #충청북도
    [(14,9), (14,11), (14,12), (13,12), (13,13)], #경상북도
    [(15,8), (17,8), (17,10), (16,10), (16,11), (14,11)], #대구
    [(17,9), (18,9), (18,8), (19,8), (19,9), (20,9), (20,10), (21,10)], #부산
    [(16,11), (16,13)], #울산
#     [(9,14), (9,15)], 
    [(27,5), (27,6), (25,6)],
]

plt.figure(figsize=(8,12))
#지역 이름 표시
for idx, row in draw_korea_raw_stacked.iterrows():
    #공백을 기준으로 2개로 나누어 진다면 줄바꿈을 해서 출력
    if len(row['ID'].split()) == 2:
        dispname = '{}\n{}'.format(
                row['ID'].split()[0],row['ID'].split()[1])
    #마지막 2글자가 고성이라면 고성이라고 출력
    elif row['ID'][:2] == '고성':
        dispname = '고성'
    else:
        dispname = row['ID']
    
    #3글자가 넘으면 폰트를 줄여서 출력
    if len(dispname.splitlines()[-1]) >= 3:
        fontsize, linespacing = 9.5, 1.5
    else:
        fontsize, linespacing = 11, 1.2

    #글자를 출력
    plt.annotate(dispname, (row['x']+0.5, row['y']+0.5),
                 weight='bold', fontsize=fontsize,
                 ha='center', va='center',
                 linespacing=linespacing)

#경계선 그리기
for path in BORDER_LINES:
    ys, xs = zip(*path)
    plt.plot(xs,ys,c='black', lw=1.5)

#상하 뒤집기 - 엑셀은 하단으로 갈때 좌표가 증가하지만
#모니터는 상단으로 갈 때 좌표가 증가합니다.
plt.gca().invert_yaxis()
#축제거
plt.axis('off')

plt.show()

#pop의 ID 와 draw_korea_raw_stacked 의 ID 불일치 찾기
print(pop.head())
print(set(draw_korea_raw_stacked['ID'].unique()) - 
      set(pop['ID'].unique()))

print(set(pop['ID'].unique()) - 
      set(draw_korea_raw_stacked['ID'].unique()))

#pop에는 있는데 draw에는 없는 데이터 제거할 리스트 만들기
del_list = list(set(pop['ID'].unique()) - 
      set(draw_korea_raw_stacked['ID'].unique()))
#리스트를 순회하면서 데이터를 제거
for rownum in del_list:
    pop = pop.drop(pop[pop['ID']==rownum].index)
#더이상 불일치한 데이터가 나오면 안됨
print(set(pop['ID'].unique()) - 
      set(draw_korea_raw_stacked['ID'].unique()))

#pop 와 draw_korea_raw_stacked 을 join
pop = pd.merge(pop,draw_korea_raw_stacked, how='inner',
               on=['ID'])
print(pop.info())

#좌표와 인구수를 가지고 pivot 테이블 만들기
mapdata = pop.pivot_table(index='y', columns='x',
                          values='인구수합계')
print(mapdata)

#NaN 제거를 위한 작업
#NaN 데이터는 -- 로 변환
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)
print(masked_mapdata)

#컬럼이름을 문자열로 설정하고 데이터프레임을 대입하고 색상명을 설정하면
#cartogram을 그려주는 메소드
def drawKorea(targetData, blockedMap, cmapname):
    gamma = 0.75

    #인구수 데이터의 크고 낮음을 분류하기 위한 값 만들기
    whitelabelmin = (max(blockedMap[targetData]) - 
                min(blockedMap[targetData]))*0.25 + \
                min(blockedMap[targetData])
    #컬럼이름을 대입하기
    datalabel = targetData
    #최대값과 최소값 구하기
    vmin = min(blockedMap[targetData])
    vmax = max(blockedMap[targetData])
    #x 와 y를 가지고 피봇 테이블 만들기
    mapdata = blockedMap.pivot_table(
            index='y', columns='x', values=targetData)
    #데이터가 존재하는 것 골라내기
    masked_mapdata = np.ma.masked_where(
            np.isnan(mapdata), mapdata)
    #그래프 영역 크기 만들기
    plt.figure(figsize=(9, 11))
    #색상 설정
    #지도에 색상을 설정
    plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, 
               edgecolor='#aaaaaa', linewidth=0.5)
    # 지역 이름 표시
    for idx, row in blockedMap.iterrows():
        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시 
        #(중구, 서구)
        if len(row['ID'].split())==2:
            dispname = '{}\n{}'.format(row['ID'].split()[0], row['ID'].split()[1])
        elif row['ID'][:2]=='고성':
            dispname = '고성'
        else:
            dispname = row['ID']

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 10.0, 1.1
        else:
            fontsize, linespacing = 11, 1.
            
        #글자색상 만들기
        annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
        #텍스트 출력하기
        plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                     fontsize=fontsize, ha='center', va='center', color=annocolor,
                     linespacing=linespacing)

    # 시도 경계 그리기
    for path in BORDER_LINES:
        ys, xs = zip(*path)
        plt.plot(xs, ys, c='black', lw=2)

    plt.gca().invert_yaxis()

    plt.axis('off')

    cb = plt.colorbar(shrink=.1, aspect=10)
    cb.set_label(datalabel)

    plt.tight_layout()
    plt.show()

#그리기
drawKorea('인구수합계', pop, 'Blues')

print(pop.head())
#소멸위기지역을 수치 데이터로 변환 - True:1, False:0
pop['소멸위기지역'] = [1 if imsi else 0 for imsi in pop['소멸위기지역']]

drawKorea('소멸위기지역', pop, 'Blues')
        
#단계구분도를 위한 라이브러리
import folium
import json

#데이터에서 지역이름을 인덱스로 설정
pop_folium = pop.set_index('ID')
print(pop_folium)

#표시하고자하는 지도의 경계선 데이터를 가져옵니다.
geo_str = json.load(open(
        './data/korea_geo_simple.json', encoding='utf-8'))
print(geo_str)

#지도 출력
map = folium.Map(location=[36.2002,127.054], zoom_start=7)

map.choropleth(geo_data = geo_str,
               data = pop_folium['인구수합계'],
               fill_color='YlGnBu',
               key_on='feature.id',
               columns=[pop_folium.index, pop_folium['인구수합계']])

map.save('pop.html')

#지도 출력
map = folium.Map(location=[36.2002,127.054], zoom_start=7)

map.choropleth(geo_data = geo_str,
               data = pop_folium['소멸위기지역'],
               fill_color='YlGnBu',
               key_on='feature.id',
               columns=[pop_folium.index, pop_folium['소멸위기지역']])

map.save('pop.html')

### 평균 구하기
s = pd.Series([10, 11, 10.78])
#비율 평균을 산술 평균으로 구하기
print(s.pct_change().mean())

import math
#평균 비율을 구할 때는 기하 평균을 사용
print(math.sqrt((11/10)*(10.78/11)) - 1)

##속도의 경우는 조화평균을 사용
#동일한 거리를 100km 와 60km로 달린 경우
print(2*100*60/(100+60))

#단순이동 평균
print(s.rolling(window=2))
#지수이동 평균
print(s.ewm(span=2))

###################################################

#descriptive.csv 파일 읽기
df = pd.read_csv('./data/descriptive.csv')
print(df.head()) #데이터가 읽어지는지 확인

df.info() #데이터의 특성 확인 - 개수, 자료형

print(df.describe()) #기술통계 확인

#gender 값의 개수만 확인
df['gender'].value_counts().plot.bar(color='k')

#이상한 데이터 확인 - 0, 5
#명목척도는 척도 이외의 값이 있으면 제거
df = df[(df['gender']==1) | (df['gender'] == 2)]
df['gender'].value_counts().plot.bar(color='k')


import random

li = list(range(1,49,1))
print(li)

random.shuffle(li)
print(li)

#비복원 추출
print(random.sample(li, k=4))

li = ['라투','오미크론','다크스펙터','나이즈']
print(np.random.choice(li, 4)) #동일한 비율로 추출
print(np.random.choice(li, 4, p=[0.05,0.3,0.15,0.5])) #동일한 비율로 추출


#행렬을 생성
#독립변수(설명변수)는 X 로 표현을 많이 합니다.
X = np.arange(20).reshape(10,2)
print(X)

#종속변수는 y로 표현을 많이 합니다.
#독립변수에 의해 값이 결정되는 것이 종속변수입니다.
#분류를 할 때는 분류될 클래스가 종속변수
y = np.arange(10)
print(y)

#성별(sex) 과 나이(age)를 가지고 생존여부(survived)를 예측
#sex, age를 묶어서 X로 생성 survived 가 y

#X 와 y에서 훈련 데이터와 시험 데이터를 분할
#훈련 데이터는 예측할 모델을 만들기 위한 데이터
#시험 데이터는 만들어진 모델을 검증하기 위한 데이터
#7:3 이나 8:2를 주로 이용

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,
        y, test_size=0.3, shuffle=True, random_state=1004)

print(X_train)
print(y_train)

#층화 무작위 추출
#계층의 비율을 적용해서 데이터를 샘플링

z = [0,0,0,1,1,1,1,1,1,1]

X_train, X_test, y_train, y_test = train_test_split(X,
        y, test_size=0.3, random_state=1008,
        stratify=z)

print(X_train)
print(y_train)






