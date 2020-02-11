#lucky02.py

import random

##함수 선언 부분##

def getNumber():
    mem = input('참석 인원을 입력해주십시오.\n')   #이렇게 하면 답 안 나옴
    return random.randint(1, int(mem))

##변수 선언 부분##
lotto = []
num = 0

##메인 프로그램 부분##

num = getNumber()
while True:
    start = input("**행운권 추첨을 시작합니다(y/n)**\n")
    if start == "n":
        break
    
    if lotto.count(num) == 0:
        lotto.append(num)
    print("당첨번호: %d" %num)
    print("당첨되셨습니다!!축하합니다\n")
