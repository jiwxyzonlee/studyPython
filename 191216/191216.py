#191216 연습문제


#Q1

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):        #매개변수 하나 더 있음
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val   #return없이 객체 변수 직접 씀

#Q2 overriding   overriding은 같은 함수 써줘야 함(덮어쓰기여서)

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100


