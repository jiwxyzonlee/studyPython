#LottoNumber

import random

print("☆★☆★ 로또 번호 자동 생성기 ★☆★☆")
print("---------------------------------------------")
print("-----------게임 수를 입력하세요-----------")

num = input("게임 수\n")

print("---------------------------------------------")

for i in range(0, int(num)):
    lotto = random.sample(range(1, 46), 6)
    lotto.sort()
    lotto = str(lotto)
    print("{0:=^22}" .format(lotto))

print("---------------------------------------------")
print("☆★☆  로또 번호 자동 생성 완료  ☆★☆")
print("---------------------------------------------")