# emp00.py

## 클래스 선언 부분 ##
class Employee:
    def __init__(self, amt):
        self.amt = amt
        
    def rise(self):
        new_amt = self.amt * 1.1
        return new_amt

