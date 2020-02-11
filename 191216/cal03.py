# cal03.py

## 클래스 선언 부분 ##
class calc:
    def __init__(self, v1, v2, op):
        self.v1 = v1
        self.v2 = v2
        self.op = op
        self.result = 0
        
    def cal(self):
        if self.op == '+':
            result = self.v1 + self.v2
        elif self.op == '-':
            result = self.v1 - self.v2
        elif self.op == '*':
            result = self.v1 * self.v2
        elif self.op == '/':
            result = self.v1 / self.v2

        return result


## 메인 코드 부분 ##
while True:
    oper = input("계산 구분을 입력하세요(+,-,*,/) : ")
    if oper == '': break

    var1 = int(input("첫 번째 수를 입력하세요 : "))
    var2 = int(input("두 번째 수를 입력하세요 : "))
    if oper == '/' and var2 == 0:
        print("0으로 나눌 수가 없습니다.\n")
        continue

    cal1 = calc(var1, var2, oper)   # 객체 cal1 생성
    res = cal1.cal()                # cal1 객체의  cal 메소스 실행

    print("계산기 : %d %s %d = %d\n" % (var1, oper, var2, res))
