#py0218.py

'''
# data를 cnt만큼 출력하는 함수
def disp(data, cnt):
    for i in range(0, cnt, 1):
        print(data)

# 함수 호출

disp('python', 3)

print()

# 매개변수 개수가 부족해서 예외
#disp('python')
#TypeError: disp() missing 1 required positional argument: 'cnt'

# 자료형 예외
#disp(3, 'python')
# TypeError: 'str' object cannot be interpreted as an integer

# 매개변수의 순서를 변경해서 대입
disp(cnt = 3, data = 'Java') #가능
print()

# cnt의 기본값이 1로 설정된 함수
# cnt를 생략하면 1
def display(data, cnt = 1):
    for i in range(0, cnt, 1):
        print(data)
        
display('C++')
'''

# sum 함수의 도큐먼트 확인
#help(sum)

'''
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
'''

# max 함수의 도큐먼트 확인
#help(max)

'''
Help on built-in function max in module builtins:

max(...)
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
'''
'''
# max의 세번째  매개변수에는 *이 붙어서 몇 개를 대입해도 됨
print(max(20, 10, 50, 40))
print(max(20, 10, 40, 50, 80, 87))
'''

'''
# **이 붙은 매개변수에는 key=value 형태로 여러 개 대입 가능
def createurl(server, port, file, **param):
    querystring = ''
    for key in param:
        querystring =querystring + key + '=' + param[key] + '&'
    url = server + ' : ' + port + '/' + file + '? ' + querystring
    print(url)

createurl('211.183.6.60', '9000', 'index.html', name='google', pw='naver')
#211.183.6.60 : 9000/index.html? name=google&pw=naver&
'''

'''
def reg(data):
    slope = 3
    intercept = 7
    return (slope, intercept)

r = reg(10)
# 튜플 한꺼번에 저장
print(r)
print(type(r))

# 튜플 나눠서 저장
slope, intercept = reg(10)
print('slope: ', slope)
print('intercept: ', slope) 
'''

'''
def fibonacci(n):
    if n == 1 or n == 2 : #끝날 때의 조건
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10)) #55
'''    
'''
def addint(x,y) :
    return x + y

# 람다식으로 바꾸기

lambdaadd = lambda x, y : x + y
print(lambdaadd(100, 200))
'''

'''
# 1000의 데이터에 1씩 더한 결과로 list 만들기

# 반복문을 이용한 방법

def inc(x):
    return x + 1

collection = [i for i in range(0, 10000, 1)]

import datetime

start = datetime.datetime.now()
print(start)

result = []
for i in collection:
    #result.append(i + 1)
    result.append(inc(i))

end = datetime.datetime.now()
print(end)

print(end-start)

#2020-02-18 19:19:30.670362
#2020-02-18 19:19:30.697243
#0:00:00.026881

collection = [i for i in range(0, 10000, 1)]

start = datetime.datetime.now()
print(start)

result = []
for i in collection:
    #result.append(i + 1)
    result.append(inc(i))

print(datetime.datetime.now())
print()

#함수형 프로그래밍을 이용한 방법
result = list(map(inc, collection))
print(datetime.datetime.now())
print(datetime.datetime.now())
'''
'''
def odd(x):
    return x % 2 == 1

li = [10, 30, 21, 32, 29]

print(filter(odd, li)) #<filter object at 0x000002191E7C7940>
print(list(filter(odd, li))) #[21, 29]


def addint(x, y):
    return x + y

#print(reduce(addint, li)) #NameError: name 'reduce' is not defined

# reduce는 누적 연산을 해서 결과를 리턴하는 함수

import functools
print(functools.reduce(addint, li)) #122
'''

