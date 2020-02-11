# emp02.py

class payment:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def rise(self):
        result = self.pay * 1.1
        return result
