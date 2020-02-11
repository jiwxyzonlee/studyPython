def cal(opr, var1, var2):
    if opr == "+":
        return var1 + var2
    elif opr == "-":
        return var1 - var2
    elif opr == "*":
        return var1 * var2
    elif opr == "/":
        return var1 / var2
    else:
        print("계산 구분을 확인해주세요.")


while True:
    opr = input("계산 구분을 입력하세요(+,-,*,/) : ")
    if opr not in ['+', '-', '*', '/']:
        print("입력값을 다시 확인해주세요")
        stop = input("종료를 원하시면 N을 입력하세요(진행을 계속 하려면 아무거나 누르세요) : ")
        if stop == 'N' or stop == 'n':
            break

    else:
        var1 = int(input("첫번째 수를 입력하세요 : "))
        var2 = int(input("두번째 수를 입력하세요 : "))
        if opr == "/" and var2 == 0:
            print("0으로 나눌 수 없습니다.")
            continue
        
 
        else:
            z = cal(opr, var1, var2)
            print("계산기 {0} {1} {2} = {3}".format(var1, opr, var2, z))
            stop = input("종료를 원하시면 N을 입력하세요(진행을 계속 하려면 아무거나 누르세요) : ")
            if stop == 'N' or stop == 'n':
                break
            
