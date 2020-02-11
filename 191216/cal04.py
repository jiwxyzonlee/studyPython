#cal04.py

#from cal05 import*

import cal05

## 메인 코드 부분 ##
while True:
    oper = input("계산 구분을 입력하세요(+,-,*,/) : ")
    if oper == '': break

    var1 = int(input("첫 번째 수를 입력하세요 : "))
    var2 = int(input("두 번째 수를 입력하세요 : "))
    if oper == '/' and var2 == 0:
        print("0으로 나눌 수가 없습니다.\n")
        continue

    cal1 = cal05.calc(var1, var2, oper)   # cal05의 calc 클래스에 객체 cal1 생성
    res = cal1.cal()                # cal1 객체의  cal 메소스 실행

    print("계산기 : %d %s %d = %d\n" % (var1, oper, var2, res))

