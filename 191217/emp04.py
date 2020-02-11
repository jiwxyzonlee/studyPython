# emp04.py

#클래스 선언 부분
class Employee:
    def  __init__(self, amt):
        self.amt = amt
    def rise(self):
        new_amt = self.amt * 1.1
        return new_amt

#메인 코드 부분
while True:
    name = input('이름을 입력하세요: ')
    if name == '': break

    pay = int(input('기존 연봉을 입력하세요: '))


    emp = Employee(pay)
    res = emp.rise()

    print('%s님의 내년 연봉은 %d 만원입니다.' %(name, res))

    
    
