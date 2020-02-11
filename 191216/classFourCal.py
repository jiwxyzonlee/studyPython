class FourCal:
    def __init__(self,first, second):
        self.first = first
        self.second = second
    #def setdata(self, first, second):  
        #self.first = first
        #self.second = second
        #self.result = 0
        #self.res = 0 #setdata에서 초기화
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first = self.second
        return result
    def div(self):
        result = self.first / self.second 
        return result   

#a = FourCal(4, 2)
#b = FourCal(3, 8)
#a.setdata(4, 3)
#b.setdata(3, 8)
#a.add()
#print(a.res)



#print(a.add())
#print(a.mul())
#print(a.sub())
#print(a.div())

"""
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
"""
#기능 개선하기01(상속)
"""
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())


print(a.add())
print(a.mul())
"""

#기능 개선하기02(오버라이딩, 덮어쓰기)-자식쪽 메소드명을 사용하게 됨

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0  #분모가 0인 경우, 숫자 0을 돌려주도록 설정
        else:
            return self.first / self.second

