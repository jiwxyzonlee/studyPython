thelist = ["+", "*", "/", "-"]

def Multiply(x, y):
    return x*y

def Divide(x, y):
    x = float(x)    #float: 소수로 변환해주는 함수)
    y = float(y)
    return x / y

def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

while True:
    operation = input("What would you like to do? \nMultiply(*)\nDivide(/)\nAdd(+)\nSubstract(-) ")
    if operation in thelist:
        break
    else:
        print("That was not an option")

if operation == "*":
    while True:
        try:               #시키려는 일, 에러가 일어날 가는성이 높음
            x = int(input("First number: "))
            break
        except ValueError:          #에러가 일어날 경우 할 일    #finally: 위에서 시키면 다 할 일
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Multiply(x, y)
    z = Multiply(x, y)
    print("%d %s %d = %d" %(x, operation, y, z))
elif operation == "-":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Subtract(x, y)
    z = Subtract(x, y)
    print("%d %s %d = %d" %(x, operation, y, z))
elif operation == "+":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number..")
    while True:
        try:
            y = int(input("Second number"))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Add(x, y)
    z = Add(x, y)
    print("%d %s %d = %d" %(x, operation, y, z))
elif operation == "/":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number,")
    while True:
        try:
            y = int(input("Second number: "))
            break
        except ValueError:
            print("Make sure to enter a number.")
    Divide(x, y)
    z = Divide(x, y)
    print("%d %s %d = %d" %(x, operation, y, z))
else:
    pass
