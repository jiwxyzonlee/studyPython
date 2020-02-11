### 2019.12.13 Won Young Jae ###

def cal(z, x, y) :
    x = int(x)
    y = int(y)
    result = 0
    if z == '+' : result = x + y
    elif z == '-' : result = x - y
    elif z == '*' : result = x * y
    else : result = x / y

    return (x, y, z, result)
    

while True :
    k = input("계산 구분을 입력하세요(+, -, *, /), 다른값 입력시 종료 : ")

    if k not in ['+', '-', '*', '/'] : break

    a = input("첫번째 수를 입력하세요 : ")
    b = input("두번째 수를 입력하세요 : ")

    if a[0] == '-' and a[1:].isnumeric() :
        pass
    elif b[0] == '-' and b[1:].isnumeric() :
        pass
    elif (a[0] == '-' and a[1:].isnumeric()) and (b[0] == '-' and b[1:].isnumeric()) :
        pass
    elif not a.isnumeric() or not b.isnumeric() :
        print("숫자를 잘못 입력하였습니다.")
        continue
    elif k == '/' and b == '0' :
        print("0으로는 나눌 수 없습니다.")
        continue
    
    a, b, k, cal_result = cal(k, a, b)
    print("계산기 : %d %s %d = %d" % (a, k, b, cal_result))
