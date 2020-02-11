thelist = ["Add", "add", "Multiply", "multiply", "Divide", "divide", "Substract", "substract"]

def Multiply(x, y):
    z = x*y
    print(z)

def Divide(x, y):
    x = float(x)    #float: 소수로 변환해주는 함수)
    y= float(y)
    z = x / y
    print(z)

def Add(x, y):
    z = x + y
    print(z)

def Subtract(x, y):
    z = x - y
    print(z)

while True:
    operation = input("What would you like to do? Multiply/Divide/Add/Substract ")
    if operation in thelist:
        break
    else:
        print("That was not an option")

if operation == "Multiply" or operation == "multiply":
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
elif operation == "subtrack" or operation == "Subtrackt":
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
elif operation == "Add" or operation =="add":
    while True:
        try:
            x = int(input("First number: "))
            break
        except ValueError:
            print("Make sure to enter a number..")
            Add(x, y)
elif operation == "Divide" or operation == "divide":
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
else:
    pass
