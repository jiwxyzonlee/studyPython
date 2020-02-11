#cal_이지원.py

def cal(a, b, symbol):
      if symbol == "+":
          result = a + b
      elif symbol == "-":
          result = a - b
      elif symbol == "*":
          result = a * b
      elif symbol == "/":
          result = a / b      
      else:
          print("Error")
      return print(a, symbol, b, "=", result)   


while True:
    a = int(input("첫번째 숫자: "))
    if list(a) in ['+', '-', '*', '.']:
          print("다시 입력해주세요")
          continue
    print("더하기( + )\n빼기( - )\n곱하기( * )\n나누기( / )")
    print()
    symbol = input("연산기호: ")
    b = int(input("두번째 숫자: "))
    cal(symbol)
    q = input("계산을 이어가시겠습니까? yes or no: ")
    if q != "yes":
        break
    





