#


"""
a = 10

a # 이 문장이 마지막이라면 출력됨
# 그렇지 않으면 출력 안 됨

b = 10

print(a)

print(a, b)
"""

#print(100)

#print(type(1000)) #자료형확인 <class 'int'>

#print(dir(1000)) #속성과 함수를 확인

"""
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__'
, '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__'
, '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__'
, '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__'
, '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__'
, '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__'
, '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__'
, '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__'
, '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__'
, '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__'
, '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__'
, '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate'
, 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
"""

#help(int.bit_length) #사용법 확인
"""
bit_length(self, /)
    Number of bits necessary to represent self in binary.
    
    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6
"""

#print((1000).bit_length()) # 몇 비트로 만들어졌는지 확인   10

"""
import sys
print(sys.path)

print(dir(list)) #list의 기능 확인
print()

list = 200
print(dir(list)) #list 정수로 바뀜. -> 식별자 쓸 때 조심
"""

"""
# 좋은 방법이 아님
print(200)  #상수값을 바로 출력

#다음에 사용할지 않을지 모르기 때문에 변수에 저장하고 사
result = 200 #200이라는 값을 result에 저장
print(result) #result의 값을 출
"""
"""
a = 10
print(a)

# 이 방식은 기존의 데이터가 없어짐
a = a + 5
print(a)

# 기존의 데이터 보존
b = 10
print(b)

c = b + 5
print(c)
"""

"""
r = 10 + 5 #숫자끼리의 덧셈은 덧셈
print(r)

k = [1,2,3] + [4,5,6] #숫자 이외의 덧셈은 결합
print(k)

# k가 sort를 가지고 있으면 호출
if sort in k:
    k.sort()

x = 6
if x in k:
    print(k[x])
else:
    print("데이터 없음")

x = 20
if x in k:
    print(k[x])
else:
    print("데이터 없음")
"""

    
