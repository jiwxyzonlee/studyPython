# emp03.py


import emp02
#from emp02 import*

fullName = input('이름을 입력하세요: ')
pay = int(input('기존 연봉을 입력하세요: '))

emp = emp02.Employee(pay)
res = emp.rise()

print('%s님의 내년 연봉은 %d 만원입니다.' %(fullName, res))
