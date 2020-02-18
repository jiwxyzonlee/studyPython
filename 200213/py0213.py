# py0213.py

"""
inp = input('정수를 입력하세요 : ')

n = int(inp)  # 정수로 변환

print(type(n)) # 자료형 확
"""

"""
gender = input('성별을 입력하세요(남자/여자) : ')

if gender == '남자':
    print('man')
    # 앞 표현식이 false여야 하면 elif, 앞 표현식과 상관 없을 시 if 사용
elif gender == '여자':
    print('woman')
else:
    print('잘못된 입력')
"""

"""
cc = input("배기량을 입력하세요 : ")
car = int(cc)

if car >= 3000:
    print('대형차')
elif 2000 <= car:
    print('중형차')
elif 1000 <= car:
    print('소형차')
else:
    print('이상한 배기량')
"""
"""
li = [100, 200, 300]
#print(dir(li))

for imsi in li:
    print(imsi)
"""
"""
print(dir(range(0, 10, 1)))
"""

'''
for imsi in range(0, 10, 1):
    print(imsi)
'''
'''
i = 1
while i <= 3:
	print('article', i)
	i = i + 1

for i in range(1, 5, 1):  #range(0, 4, 1) 도 가능
	print('num=', 1 + 15 * (i-1))
	# range(0, 4, 1)의 경우 print('num=', 1 + 15 * i)
'''
'''
for i in range(1, 4, 1):
	if i % 2 ==0:
		print(i)
		break
else:
	print('반복문을 전부 수행')


for i in range(1, 4, 1):
	if i % 4 ==0:
		break
else:
	print('반복문을 전부 수행')
'''

li = [100, 300, 200]

#print(li.sort()) # 잘못된 문장 - sort는 리턴을 하지 않아 None 출력

li.sort()

print(li) # 데이터에 작업한 것을 알 수 있음 [100, 200, 300]



