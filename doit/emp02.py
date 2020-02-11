# emp02.py

"""
class payment:
    def __init__(self, pay):
        #self.name = name
        self.pay = pay
    def rise(self):
        result = self.pay * 1.1
        return result
"""

#클래스 선언 부분
class Employee:
    def  __init__(self, amt):
        self.amt = amt
    def rise(self):
        new_amt = self.amt * 1.1
        return new_amt
