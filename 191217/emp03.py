# emp03.py
import emp00

## 메인 코드 부분 ##
while True:
    name = input("이름을 입력하세요: ")
    if name == '': break

    pay = int(input("기존 연봉을 입력하세요 : "))

    emp1 = emp00.Employee(pay)
    res = emp1.rise()

    print("%s님의 내년 연봉은 %d 만원 입니다.\n" % (name, res))
