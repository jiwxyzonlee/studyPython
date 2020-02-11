#fibo.py

#피보나치 수열을 위한 모듈

def fib(n):                         #n까지 피보나치 수열을 출력하는 함수
    a, b = 0, 1
    while b < n:
        print(b, end= ' ')  #end 기본값인 줄 넘기기 대신 공백으로 한 줄에 출력
        a, b = b, a + b
        print()

def fib2(n):                    #n가지의 피보나치 수열을 반환하는 함수
    result = []                   #피보나치 수 저장을 위한 리스트 초기화
    a, b = 0, 1
    while b <  n:
        result.append(b)    #리스트 값 채우기
        a, b = b, a + b
    return result               #피보나치 수 리스트 반환
