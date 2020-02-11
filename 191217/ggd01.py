# ggd01.py

"""
def GuGu(n):
    result = []
    i = 1

    while i <10:
        result.append(n * i)
        i = i + 1
    return result
print(GuGu(2))
"""
"""
def GuGu(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result
dan = int(input("몇 단을 계산할까요?"))
print(GuGu(dan))

"""

class GGD:
    def __init__(self, i):
        self.i = i
    def GuGu(self):
        result = []
        for j in range(1, 10):
           result.append(self.i * j)
        return result

while True:
    num = int(input("구구단: 숫자를 입력하세요\n"))
    if num == '':
              continue
    else:
        ggd = GGD(num)
        gugu = ggd.GuGu()
        print(gugu)
        print()

