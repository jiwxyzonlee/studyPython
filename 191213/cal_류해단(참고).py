import re
operList = ('+','-','*','/')
def cal(oper, var1, var2):
    #for oper1 in operList:
    #    if oper == operList[0]:
    #        return var1 + var2
    #    elif oper == operList[1]:
    #        return var1 - var2
    #    elif oper == operList[2]:
    #        return var1 * var2
    #    elif oper == operList[3]:
    if oper == "+":
        return var1 + var2
    elif oper == "-":
        return var1 - var2
    elif oper == "*":
        return var1 * var2
    elif oper == "/":
        return var1 / var2
    
#에러메시지   
def errMes(var):
    print('숫자만 입력 가능합니다.'.format(var))

#계산 구분 입력 안할 경우 종료
#% 시 0으로 할경우 종료
while True:

    #1.계산 구분 판단
    oper2= ""
    while True:
        oper= input("계산 구분을 입력하세요")
        
        if oper not in operList:
            print("정확한 계산 구분을 입력하여주세요.")
            continue
        else:
            break
            

    #숫자입력
    var1 = 0
    while True:
        try:            
            var1= int(input("첫 번째 수를 입력하세요. : "))
        except ValueError :  # 에러 종류
            errMes(var1)
            continue
        break
    var2 = 0   
    while True:
        try: 
            var2= int(input("두 번째 수를 입력하세요. : "))
            if oper=="/" and var2== 0:
                print("두번째 수를 확인하여 주십시요. : ")
                continue
            else:
                break
        except ValueError :  # 에러 종류
            errMes(var2)
            continue
        break
    
    result= cal(oper, var1, var2);
    print("계산기 : %d %s %d = %d" % (var1,oper,var2,result))

    result = input("enter 눌릴 겨우 종료됩니다.")

    if result == '':
        print("계산기 종료합니다.")
        break
    else:
        print("계산기 진행됩니다.")

    
