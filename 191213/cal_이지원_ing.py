#cal_이지원.py

def cal(i, k, j):
      if j == "+": result = i + k
      elif j == "-": result = i - k
      elif j == "*": result = i * k
      elif j == "/": result = i / k      
      else:
          print("Error")
      return print(i, j, k, result)   


while True:
      j = input("연산기호: ")

      if j not in ['+', '-', '*', '/']

      var1 = input("첫번째 숫자: ")
      var2 = input("두번째 숫자: ")
   
    
    if list(a) in ['+', '-', '*', '.']:
          print("다시 입력해주세요")
          continue
    print("더하기( + )\n빼기( - )\n곱하기( * )\n나누기( / )")
    print()
    j = input("연산기호: ")
    b = int(input("두번째 숫자: "))
    cal(symbol)
    q = input("계산을 이어가시겠습니까? yes or no: ")
    if q != "yes":
        break
    





