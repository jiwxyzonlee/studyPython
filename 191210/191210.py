


 #interpreter
 #한 줄 단위 코딩
 #바로 번역

 #complier
 #전체 소스 한꺼번에
 #compile 이후 실행 파일 exe
 #실행하는 데 빠름

#파이썬은 꼭 레벨에 맞게끔 줄을 맞춰야 함

 #>>> (prompt)

#파이썬 기본 화면이 인터프리터(파이썬 셸)

#변수 생성은 메모리에 저장

#변수가 메모리 위치 알려줌

#if 끝에는 반드시 :
#for 반복문
#while 반복문

a = 3

if a > 1:
	print("a is greater than 1")

for a in [1, 2, 3]:
	print(a)

	
i = 0

while i <3:
	i = i + 1
	print(i)


#def는 함수를 만들 때 사용하는 예약어
 def sum(a, b):
	return a + b

print(sum(3, 4))

#여러줄로 이루어진 주석은 큰따옴표 세 개 사이에 주석문을 작성하면 된다
 """여러줄로 이루어진 주석은
큰 따옴표 세개 사이에
주석문을 작성하면 된다"""
'여러줄로 이루어진 주석은\n큰 따옴표 세개 사이에\n주석문을 작성하면 된다'
#불 자료형: 참/거짓
 #변수 자료 대입 -> 메모리 = 변수
 #파이썬은 자료형이 반이다
 """실수 123.45, -1234.5, 3.4e10

8진수 0o34, 0o25

16진수 0x2A, 0xFF
'실수 123.45, -1234.5, 3.4e10\n\n8진수 0o34, 0o25\n\n16진수 0x2A, 0xFF'"""
#대입연산(+=, -=, *=, /=)
a += 1   #(a = a +1)

a -= 1  # a = a - 1

a  = 3
print(a)

a = 3
b = 4

#a**b #a의 b승

#7%3 #나머지

#3%7 #나머지

#7//3 #몫

#7//4 #몫

#몫이랑 나머지는 페이지 나눌 때 유용

"""문자열에 큰따옴표(“) 포함시키기
 문자열을 작은따옴표(‘)로 둘러싸야 함
 작은따옴표(‘) 안에 사용된 큰따옴표는(“)는 문자열을 만드는 기호로 인식되지 않음
say = '"Python is very easy." he says.' """
'문자열에 큰따옴표(“) 포함시키기\n\uf0fc 문자열을 작은따옴표(‘)로 둘러싸야 함\n\uf0fc 작은따옴표(‘) 안에 사용된 큰따옴표는(“)는 문자열을 만드는 기호로 인식되지 않음\nsay = \'"Python is very easy." he says.\' '
"""백슬래시(\)를 이용해서 작은따옴표(‘)와 큰따옴표(“)를 문자열에 포함시키기
 백슬래시(\)를 작은따옴표(‘)나 큰따옴표(“) 앞에 삽입하면 백슬래시(\) 뒤의 작은따옴표(‘)나 큰따옴표(“)는 문자열을 둘러싸는 기호의 의미가 아니라 (‘), (“) 그 자체를 의미함
\뒤는 문자열"""
'백슬래시(\\)를 이용해서 작은따옴표(‘)와 큰따옴표(“)를 문자열에 포함시키기\n\uf0fc 백슬래시(\\)를 작은따옴표(‘)나 큰따옴표(“) 앞에 삽입하면 백슬래시(\\) 뒤의 작은따옴표(‘)나 큰따옴표(“)는 문자열을 둘러싸는 기호의 의미가 아니라 (‘), (“) 그 자체를 의미함\n\\뒤는 문자열'
food = 'Python\'s favorite food is perl'
 

food = 'Python\'s favorite food is perl'
food
"Python's favorite food is perl"
say = "\"Python is very easy.\" he says."
say
'"Python is very easy." he says.'
#줄을 바꾸는 이스케이프 코드 ‘\n’ 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

"""문자열 인덱싱과 슬라이싱
인덱싱(Indexing)이란 무엇인가를 가리킨다는 의미이고, 슬라이싱(Slicing)은 무엇인가를
잘라낸다는 의미임
변수 a에 저장한 문자열의 각 문자마다 번호를 매겨보면 다음과 같음"""
'문자열 인덱싱과 슬라이싱\n인덱싱(Indexing)이란 무엇인가를 가리킨다는 의미이고, 슬라이싱(Slicing)은 무엇인가를\n잘라낸다는 의미임\n변수 a에 저장한 문자열의 각 문자마다 번호를 매겨보면 다음과 같음'
multiline = '''
life is too short
you need python
'''
print(multiline)


head = "Python"
tail = "is fun!"
head + tail
'Pythonis fun!'

a = "python"
a*2
'pythonpython'
# *는 문자열의 반복
# a*2 는 두 번 반복
#문자열 길이
a = "Life is too short"
len(a)

"""문자열 인덱싱과 슬라이싱
인덱싱(Indexing)이란 무엇인가를 가리킨다는 의미이고, 슬라이싱(Slicing)은 무엇인가를
잘라낸다는 의미임
변수 a에 저장한 문자열의 각 문자마다 번호를 매겨보면 다음과 같음"""
'문자열 인덱싱과 슬라이싱\n인덱싱(Indexing)이란 무엇인가를 가리킨다는 의미이고, 슬라이싱(Slicing)은 무엇인가를\n잘라낸다는 의미임\n변수 a에 저장한 문자열의 각 문자마다 번호를 매겨보면 다음과 같음'
a[3]
'e'
 a[0]
'L'
a[12]
's'
a[-1]
't'
a[-0]
'L'
#1부터 시작하는 R과 달리 파이썬은 0부터 시작함
#a[-1]a[-1]은 문자열을 뒤에서부터 읽기 위해서 마이너스(-)를 붙임
"""슬라이싱 기법으로 간단하게 처리할 수 있음
 a[시작 번호:끝 번호]를 지정하면, a문자열에서 자리번호 0부터 지정번호까지의 문자를
뽑아낸다는 뜻
 끝 번호에 해당하는 것은 포함되지 않는 것에 주의"""
'슬라이싱 기법으로 간단하게 처리할 수 있음\n\uf0fc a[시작 번호:끝 번호]를 지정하면, a문자열에서 자리번호 0부터 지정번호까지의 문자를\n뽑아낸다는 뜻\n\uf0fc 끝 번호에 해당하는 것은 포함되지 않는 것에 주의'
>>> 
>>> 
>>> a[19: ]
''
>>> a[19:]
''
>>> a = "Life is too short"
>>> a[19: ]
''
>>> a[19:]
''
>>> a = "Life is too short"
>>> a[19:]
''
>>>  a[:17
   
SyntaxError: unexpected indent
>>>  a[:17]
 
SyntaxError: unexpected indent
>>> a[:17]
'Life is too short'
>>> 
a[-0] # = a[0]
'L'
>>>  a[0:4]
 
SyntaxError: unexpected indent
>>> a[0:4]
'Life'
>>>  #0 <= a < 4
>>> a[:]
'Life is too short'
>>> a = "Life is too short, You need Python"
>>> len(a)
34
>>> a[19:-7]
'You need'
>>> a[-8]
'd'
>>> a[-7]
' '
>>> a[-0] # = a[0]
'L'
>>> 
>>> 
>>> a = "20010331Rainy"
>>> 
>>> date = a[:8]
>>> weather = a[8:]
>>> 
>>> date
'20010331'
>>> weather
'Rainy'
>>> 
>>> yyyy = a[:4]
>>> mm = a[4:6]
>>> dd = a[6:8]
>>> 
>>> yyyy
'2001'
>>> mm
'03'
>>> dd
'31'
>>> 
>>> 
>>> #문자열 바꾸기
>>> #‘Pithon’ 이라는 문자열을 ‘Python’으로 바꾸려면?
>>> 
>>> 
>>> a = 'Pithon'
>>> 
>>> a[1]
'i'
>>> a[1] = 'y'  #에러남
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a[1] = 'y'  #에러남
TypeError: 'str' object does not support item assignment
>>> 
>>> b = a[:1} + 'y' + a[2:]
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> b = a[:1] + 'y' + a[2:]
>>> 
>>> a
'Pithon'
>>> b
'Python'
>>> 
>>> 
>>> #문자열 포매팅
>>> #문자열은 같은데 특정값만 바꿔야 할 때
>>> 
>>> #%d  d는 숫자
>>> 
>>> #% 포맷 코드 %뒤에는 숫자
>>> 
>>> 
>>>  "I eat %d apples." %3 #%d: 문자열 포맷코드
 
SyntaxError: unexpected indent
>>> "I eat %d apples." %3 #%d: 문자열 포맷코드
'I eat 3 apples.'
>>> 
>>> #%s  s는 문자
>>> 
>>> "I eat %s apples." %"five"
'I eat five apples.'
>>> 
>>> 
>>> #변수 바로 대입도 가능
>>> 
>>> number = 3
>>> 
>>> "I eat %d apples." %number
'I eat 3 apples.'
>>> 
>>> #2개 이상 가능
>>> 
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. so I was sick for %s days." %(number,day)
'I ate 10 apples. so I was sick for three days.'
>>> 
>>> "I eat %d apples and %s pears." %(3, "five") #그냥 해도 가능, 순서만 안 바뀌면
'I eat 3 apples and five pears.'
>>> 
>>> 
>>> #%s 포맷 코드는 어떤 형태의 값이든 변환해서 넣을 수 있음
>>> 
>>> #포맷팅 연산자 %d와 %를 같이 쓸 때는 %%를 씀
>>> 
>>> "Error is %d%." %98
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    "Error is %d%." %98
ValueError: incomplete format
>>> "Error is %d%%." %98
'Error is 98%.'
>>> # %% 꼭 두개
>>>  """#문자열 포맷팅 코드인 %d와 %가 문자열 내에 존재하는 경우, %를 나타내려면
반드시 %%로 써야함"""
 
SyntaxError: unexpected indent
>>> """문자열 포맷팅 코드인 %d와 %가 문자열 내에 존재하는 경우, %를 나타내려면
반드시 %%로 써야함"""
'문자열 포맷팅 코드인 %d와 %가 문자열 내에 존재하는 경우, %를 나타내려면\n반드시 %%로 써야함'
>>> 
>>> 
>>> "%d%%hello." %30
'30%hello.'
>>> 
>>> 
>>> """%10s는 전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고, 그 앞의 나머지는 공백으로 남겨두라는 의미임"""
'%10s는 전체 길이가 10인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고, 그 앞의 나머지는 공백으로 남겨두라는 의미임'
>>> #반대로는 -10
>>> 
>>> #%10s%"hi
>>> %10s%"hi"
SyntaxError: invalid syntax
>>>  "%10s"%"hi"
 
SyntaxError: unexpected indent
>>> "%10s"%"hi"
'        hi'
>>> 
>>> "%-10s" % "hi"
'hi        '
>>> 
>>> "%-10sjane" % "hi"
'hi        jane'
>>> 
>>> 
>>> "%-10shi" % "jane"
'jane      hi'
>>>  #10에서 s만큼 빠짐
>>> 
>>> #소수점 표현하기
>>> # 0.4f 소수점 네 자리까지
>>> 
>>> # %10.4f 소수점 네 자리까지 한 후 오른쪽 정렬
>>> 
>>> 
>>> "%0.4f" % 3.42134234
'3.4213'
>>> 
>>> "%10.4f" % 3.4134234
'    3.4134'
>>> 
>>> 
>>> #format 함수를 사용한 포맷팅
>>> #숫자 바로 대입하기
>>> # "I eat {0}  <<변수가 하나일 땐 0, 두 개일 때는 1
>>> 
>>> # "I ate {0}apples and {1}days
>>> 
>>> "I eat {0} apples" .format(3)"
SyntaxError: EOL while scanning string literal
>>> "I eat {0} apples" .format(3)"
SyntaxError: EOL while scanning string literal
>>> "I eat {0} apples." .format(3)
'I eat 3 apples.'
>>> 
>>>  "I eat {0} apples" .format("five")
 
SyntaxError: unexpected indent
>>> "I eat {0} apples" .format("five")
'I eat five apples'
>>> 
>>> 
>>> number = 3
>>> day = "three"
>>> "I ate {0} apples. so I was sick for {1} days." .format(number, day)
'I ate 3 apples. so I was sick for three days.'
>>> 
>>> "I ate {number} apples. So I was sick for {day} days." .format(number = 10, day = 3)
'I ate 10 apples. So I was sick for 3 days.'
>>> 
>>> "I ate {number} apples. So I was sick for {day} days." .format(number = 10, day = "three")
'I ate 10 apples. So I was sick for three days.'
>>> 
>>> "I ate {number} apples. So I was sick for {day} days." .format(day = 3, number = 10)
'I ate 10 apples. So I was sick for 3 days.'
>>> #이 때는 순서바뀌어도 ok
>>> 
>>> 
>>> "I ate {0} apples. So I was sick for {day} days." .format(10, day=3)
'I ate 10 apples. So I was sick for 3 days.'
>>> 
>>> "I ate {0} apples. So I was sick for {day} days." .format("ten" , day=3)
'I ate ten apples. So I was sick for 3 days.'
>>> #{0} 이어도 "ten" 들어감
>>> 
>>> "I ate {0} apples. So I was sick for {day} days." .format(day=3, "ten")
SyntaxError: positional argument follows keyword argument
>>> 
>>> #이건 순서 바뀌면 안됨
>>> 
>>> 
>>> #문자열 정렬
>>> #공백 0에서 9까지 정렬 0:<10
>>> 
>>> #왼쪽 정렬 <
>>> 
>>> "{0:<10}" .format("hi")
'hi        '
>>>     #비교
>>> "%10s"%"hi"
'        hi'
>>> #오른쪽 정렬 >
>>> "{0:>10}" .format("hi")
'        hi'
>>> 
>>> 
>>> #가운데 정렬 ^
>>> "{0:^10}" .format("hi")
'    hi    '
>>> 
>>> 
>>> #정렬 후 여백 채우기
>>> 
>>> "{0:=^10} .format("hi")
SyntaxError: invalid syntax
>>> "{0:=^10} .format("hi")
SyntaxError: invalid syntax
>>> "{0:=^10} .format("hi")
SyntaxError: invalid syntax
>>> "{0:=^10} .format("hi")
SyntaxError: invalid syntax
>>> "{0:=^10}" .format("hi")
'====hi===='
>>> "{0:!<10}" .format("hi")
'hi!!!!!!!!'
>>> #왼쪽 정렬 !로 채우기
>>> 
>>> y = 3.42134234
>>> "{0:0.4f}" .format(y)
'3.4213'
>>> 
>>> "{0:10.4f}" .format(y)
'    3.4213'
>>> #오른쪽 정렬 후 소수점 네자리
>>> 
>>> 
>>> "{{ and }}" .format()
'{ and }'
>>> #문자 표현하기
>>> 
>>> 
>>> "{0:^10}" .format("^-^")
'   ^-^    '
>>> "{0:★^10}" .format("^-^")
'★★★^-^★★★★'
>>> 
>>> 
>>> # f문자열 포매팅
>>>  # new!
 
>>> #이건 딕셔너리도 가능
>>> name = '홍길동'
>>> age = 30
>>> 
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> f'나는 내년이면 {age + 1}살이 된다.'
'나는 내년이면 31살이 된다.'
>>> 
>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {["age"]}입니다.'
"나의 이름은 홍길동입니다. 나이는 ['age']입니다."
>>> d = {'name':'홍길동', 'age':'30'}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {["age"]}입니다.'
"나의 이름은 홍길동입니다. 나이는 ['age']입니다."
>>> d = {'name':'홍길동', age:30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {["age"]}입니다.'
"나의 이름은 홍길동입니다. 나이는 ['age']입니다."
>>> 
>>> d = {'name':'홍길동'. 'age':30}
SyntaxError: invalid syntax
>>> d = {'name':'홍길동'. 'age':30}
SyntaxError: invalid syntax
>>> d = {'name':'홍길동', 'age':30}
>>> f’나의 이름은 {d[“name”]}입니다. 나이는 {d[“age”]}입니다.’
SyntaxError: invalid character in identifier
>>> f’나의 이름은 {d[“name”]}입니다. 나이는 {d[“age”]}입니다.’
SyntaxError: invalid character in identifier
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> 
>>> 
>>> 
>>> #정렬
>>> 
>>> f'{"hi": <10}'
'hi        '
>>> f'{"hi":>10}'
'        hi'
>>> f'{"hi":^10}'
'    hi    '
>>> 
>>> 
>>> #공백 채우기
>>> f'{"hi":=^10}'
'====hi===='
>>> 
>>> f'{"hi":★<10}'
'hi★★★★★★★★'
>>> 
>>> 
>>> #소수점 표현하기
>>> 
>>> y = 3.42134234
>>> 
>>> f'{y:0.4f}'
'3.4213'
>>> 
>>> f'{y:10.4f}'
'    3.4213'
>>> 
>>> 
>>> f'{{ and }}'
'{ and }'
>>> 
>>> 
>>> # 'a' 라는 객체에서 'b'가 몇개인가
>>> 
>>> a = "hobby"
>>> a.count('b')
2
>>> 
>>> #a 라는 변수중에서 알파벳b가 몇 번째에 있냐
>>> a.find('b')
2
>>> 
>>> a= "Python is the best choice
SyntaxError: EOL while scanning string literal
>>> a= "Python is the best choice
SyntaxError: EOL while scanning string literal
>>> a= "Python is the best choice"
>>> 
>>> a.find('b')
14
>>> 
>>> a.find('k')
-1
>>> #없을 시 -1 값 뜸
>>> 
>>> #find = index
>>> #find는 없는 값 ; -1, index는 에러 뜸
>>> 
>>> a.index('t')
2
>>> a.index('k')
Traceback (most recent call last):
  File "<pyshell#425>", line 1, in <module>
    a.index('k')
ValueError: substring not found
>>> ValueError: substring not found
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> #문자열 삽입
>>> #a.join('abcd')
>>> 
>>> 
>>> 
>>> #a.find 대소문자 구분함(파이썬 물론)
>>> 
>>> 
>>> a = ","
>>> a.join('abcd')
'a,b,c,d'
>>> 
>>> 
>>> #소문자 ->대문자 upper
>>> #대문자 -> 소문자 lower
>>> 
>>> a="hi"
>>> 
>>> a.upper()
'HI'
>>> 
>>> 
>>> a = "HI"
>>> 
>>> a.lower()
'hi'
>>> 
>>> 
>>> #왼쪽공백 지우기 lstrip
>>> 
>>> 
>>> a = "         hi    "
>>> 
>>> a. lstrip()
'hi    '
>>> 
>>> 
>>> a = "         hi    "
>>> 
>>> a.rstrip()
'         hi'
>>> 
>>> a = "         hi    "
>>> 
>>> a.strip()
'hi'
>>> 
>>> #strip 함수 자주 씀
>>> 
>>> 
>>> #단어 바꾸기
>>> #a.replace("Life", Your leg")
>>> 
>>> a = "Life is too short"
>>> a.replace("Life","Your leg")
'Your leg is too short'
>>> 
>>> 
>>> 
>>> #split 문자열 쪼개기
>>> 
>>> #a.split( ): 스페이스를 기준으로 나눠라
>>> 
>>> a = "Life is too short"
>>> 
>>> a.split()
['Life', 'is', 'too', 'short']
>>> 
>>> 
>>> 
>>> a = "a:b:c:d"
>>> 
>>> a.split(':')
['a', 'b', 'c', 'd']
>>> # : 기준으로 쪼개기
>>> 
>>> 
>>> #리스트를 사용하면 1, 3, 5, 7, 9 숫자 모음을 간단하게 표현할 수 있음
>>> 
>>> 
>>> odd = [1, 3, 5, 7, 9]
>>> 
>>> #리스트를 만들 때는 대괄호([ ])로 감싸 주고, 각 요소 값들은 쉼표(,)로 구분해 줌
>>> 
>>> #리스트명 = [요소1, 요소2, 요소3, ···]
>>> 
>>> 
>>> a = [1, 2, 3]
>>> 
>>> type(a)
<class 'list'>
>>> #변수의 타입
>>> 
>>> a = "python"
>>> type(a)
<class 'str'>
>>> 
>>> #string 문자열이다
>>> 
>>> a = [1, 2, 3]
>>> 
>>> a = [1,2,3]
