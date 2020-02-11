# cal02.py

## 함수 선언 부분 ##
def cal(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2

    return result


## 메인 코드 부분 ##
while True:
    oper = input("계산 구분을 입력하세요(+,-,*,/) : ")
    if oper == '': break

    var1 = int(input("첫 번째 수를 입력하세요 : "))
    var2 = int(input("두 번째 수를 입력하세요 : "))
    if oper == '/' and var2 == 0:
        print("0으로 나눌 수가 없습니다.\n")
        continue

    res = cal(var1, var2, oper)

    print("계산기 : %d %s %d = %d\n" % (var1, oper, var2, res))
