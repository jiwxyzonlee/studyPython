# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 현재 디렉토리 확인
import os

print(os.getcwd())

# numpy import
# numpy를 np라는 이름으로 사용 (numpy라는 이름으로 사용 못함)
import numpy as np

# list
li = [100, 300, 200]
#print(dir(li))

ar = np.array(li)
print(ar)

tu  = (100, 200)
#print(dir(tu))

ar = np.array(tu)
print(ar)

# 서로 다른 자료형의 데이터가 모여있으면 동일한 자료형으로 변경됨
ar = np.array([[100, 200, 300], [400, 500, 600]])
print(ar)

# 각 요소의 자료형
print(ar.dtype)

#dtype을 설정해서 정수 배열로 만들기
ar = np.array([[100, 200, 300], [400, 500, 600]], dtype = int)
print(ar)

#각 요소의 자료형
print(ar.dtype)

print(ar.ndim) # 전체 차원을 리턴
print(ar.shape) # 각 차원의 데이터 개수를 튜플로 리턴

# 일정한 숫자 패턴의 array 생성
ar = np.arange(0, 100, 1)
print(ar)

# linspace는 기본적으로 stop이 포함됨
# 마지막 숫자를 제거하고자 하면 endpoint를 False를 설정

ar = np.linspace(0, 10, num = 11)
print(ar)

# 단위 행렬 만들기(대각선 방향의 요소만 1인 행렬)
# 정방 행렬 - 행과 열의 개수가 같은 행렬
# 단위 행렬은 정방행렬이어야 함

# 크기가 3인 단위 행렬 생성
ar = np.eye(3)
print(ar)

# 1의 위치를 1개 증가
ar = np.eye(3, k = 1)
print(ar)

# 대각 요소만 뽑아서 1차원 배열을 생
ar = np.diag(ar)
print(ar)

# 희소행렬과 밀집행렬 변환
import numpy as np

# scipy의 sparse 모듈 가져오기
from scipy import sparse

# 5*5 단위 행렬 생성
ar = np.eye(5)
print(ar)

# 희소행렬로 변환 - 0이 아닌 값의 위치와 값을 저장
sp = sparse.csr_matrix(ar)
print(sp)

#밀집 행렬로 변환
ar = sp.toarray()
print(ar)

# 행렬의 차원 변환
# 0~9까 10개의 요소로 된 배열 생성

ar = np.arange(0, 10)
print(ar)

# 행 2개 열5개 배열로 변환
print(ar.reshape(2, 5))


# 인덱싱과 copy
import numpy as np
ar = np.array([100, 200, 300, 400])

# 0-1번까지 요소를 br에 대입
br = ar[0:2]
print(br)

# 원본 데이터를 변경 ar의 데이터를 변경하면 br의 데이터도 변경

ar[0] = 10000
print(br)

# 데이터를 복사해서 전달
cr = ar[0:2].copy()
print(cr)


# 원본을 변경하면 br은 변경되지만 cr은 변경이 안됨
ar[0] = 1300
print(br) #[1300  200]
print(cr) #[10000   200]


# 쓰레기 값을 가지고 배열을 생성

ar = np.empty((10, 5))
print(ar)

# 행들을 선택 - 0,1,3,5
br = ar[[0, 1, 3, 5]]
print(br)

# 현재는 같은 값을 가지고 있음
print(ar[0, 0])
print(br[0, 0])

# copy가 되었으므로 ar의 데이터가 변경되더라도
# br의 데이터는 영향을 받지 않음
ar[0, 0] = 90
print(ar[0, 0])
print(br[0, 0])

# 3, 5행과 0, 2 열의 데이터 추출
cr = ar[[3, 5], [0, 2]]
# 3,0과 5,2번만 추출
print(cr)
# 3,5번행 그리고 0,2번 열 선택
dr = ar[np.ix_([3, 5], [0, 2])]
print(dr)

# 행과 열의 순서 변경
ar = np.arange(0, 16)
print(ar)

# 2차원 배열로 전환
br = ar.reshape(4, 4)
print(br)
# 행렬 변환 - 2차원은 T나 transpose 가 동일
print(br.T)
print(br.transpose())

# 3차원으로 변환
cr = ar.reshape((2, 2, 4))
print(cr)
# 4, 2, 2로 변경
print(cr.transpose())
# 2, 4, 2로 변경
print(cr.transpose(0, 2, 1))


# 배열의 모든 요소에게 함수를 적용해서 새로운 배열 만들기
ar = np.arange(0, 5)

# 위의 배열에 전부 5를 더한 결과를 가지고 새로운 배열을 생성
def plus5(x):
    return x + 5

# 벡터화된 함수를 생성
#vec_func = np.vectorize(plus5)   
# 람다 함수 이용
vec_func = np.vectorize(lambda x:x+5)

# 벡터화된 함수를 적용
result = vec_func(ar)
print(result)

# ndarray가 가진 속성과 메소드 확인
print(dir(np.ndarray))


# 동일한 차원의 동일한 크기의 배열 연산
# 각 요소마다 연산해서 동일한 크기의 배열로 리턴
import numpy as np

ar = np.arange(1, 6)
# 100부터 105까지 5개로 분할하는데 마지막 숫자는 미포힘
br = np.linspace(100, 105, num = 5, endpoint = False)

#print(ar)
#print(br)

# 덧셈 => 숫자 배열
result = ar + br
print(result) # 각각 더해서 배열로 리턴 [101. 103. 105. 107. 109.]

# 크기 비교 => bool 배열
result = ar > br
print(result) # [False False False False False]

# 논리 연산
# 0이 아닌 숫자는 True
result = np.logical_xor(ar, br)
print(result)


# 차원이 다른 배열의 연산 - Broadcast
ar = np.array([100, 200, 240])

# 배열의 각 요소에서 100을 뺀 후 배열로 리턴
result = ar - 100
print(result)

br = np.arange(0, 6)
cr = br.reshape(2, 3)
print(cr)

result = ar + cr
print(result)

dr = br.reshape(3, 2)
#result = ar + dr
#print(result)


# boolean 색인
ar = np.array([100, 200, 301, 28])

print(ar % 2 == 0) #[ True  True False  True]

# 배열의 인덱스 자리에 bool 배열을 대입하면 True인 데이터만 리턴
print(ar[ar % 2 == 0]) #[100 200  28]


# 난수 생성
import numpy as np

#배열 생성
ar = np.arange(0, 48)
#print(ar)
# 배열의 데이터 순서를 랜덤하게 배치
np.random.shuffle(ar)
print(ar)

# 5개의 랜덤한 숫자를 추출
print(np.random.normal(size = 5))
# seed 고정
# 실행할 때마다 동일
np.random.seed(seed = 100)
# 5개의 랜덤한 숫자를 추출
print(np.random.normal(size = 5))

# 기본통계 함수
ar = np.arange(1, 10)
ar = ar.reshape(3, 3)
print(ar)

# 모든 데이터를 더한 결과
print(np.sum(ar)) #45

# 행 단위, 열단위로 합계
# axis 옵션은 차후로도 동일한 용도로 사용되므로 기억
print(np.sum(ar, axis = 0)) #열 [12 15 18]
print(np.sum(ar, axis = 1)) #행 [ 6 15 24]

# 2개의 배열에서 데이터를 골라 새로운 배열 만들기
ar = np.array([100, 200, 300, 400])
br = np.array([101, 201, 301, 401])
cond = np.array([True, False, False, True])

# cond 값이 True이면 ar에서, False이면 br에서 추출
result = np.where(cond, ar, br)
print(result)


# 데이터 정렬
import numpy as np

ar = np.array([30, 200, 300, 400, 210, 40])
result = np.sort(ar)
print(result)
print(ar)

help(np.sort)
help(ar.sort)
"""kind : {'quicksort(가장 빠름)', 'mergesort(합쳐가 sort)', 'heapsort(분할 sort)', 'stable'}
, optional Sorting algorithm. Default is 'quicksort'. """

br = ar.reshape(2, 3)
print(br)
br.sort(axis = 1) # 1이면 행단위로, 0이면 열단위
print(br)







