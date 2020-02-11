#classCalc_이지원.py

#class 선언 부분
class Calc:
    def __init__(self, v1, v2, op):      #생성자 반드시 있어야
        self.v1 = v1                           #일반 변수가 객체 변수로 바뀜
        self.v2 = v2
        self.op = op
    def cal(self):
        result = 0
        if self.op == '+':
            result = self.v1 + self.v2
        elif self.op == '-':
            result = self.v1 - self.v2
        elif self.op == '*':
            result = self.v1 * self.v2
        elif self.op == '/':
            try:
                result = self.v1 / self.v2
            except ZeroDivisionError:
                print("0으로 나눌 수 없습니다")
        return result


#메인 코드 부분

while True:
    oper = input('계산 구분을 입력하세요(+, - , *, /): ')
    if oper == '': break

    var1 = int(input('첫번째 수를 입력하세요: '))
    var2 = int(input('두번째 수를 입력하세요: '))

    cal1 = Calc(var1, var2, oper) #def __init__까지 수행
    res = cal1.cal()
    print("계산기 : %d %s %d = %d\n" %(var1, oper, var2, res))
    #break
               
       
    
        
