#lotto.py


import random
def getNumber():
    return random.randrange(1, 46)

##변수 선언 부분##
lotto = []
num = 0

##메인프로그램 부분##
print("**로또 추첨을 시작합니다**")

while True:
    num = getNumber()

    if lotto.count(num) == 0:  #count (table 같은 거)
        lotto.append(num)

    if len(lotto) >= 6:
        break
print("당첨된 로또 번호 :", end = ' ')
lotto.sort()
for i in range(0,6):
    print("%d" %lotto[i], end = ' ')
    
