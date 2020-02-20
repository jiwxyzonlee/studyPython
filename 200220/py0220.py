# py0220.py

'''
# 클래스 생성
class Student:
    # member 메소드
    def func(self):
        print('member method')

obj = Student()
obj.func()  # 인스턴스가 메소드를 호출 - 권장
Student.func(obj) # 클래스가 메소드를 호출
'''

'''
class Student:
    # 이 변수는 클래스와 인스턴스 모두 접근 가능하지만
    # 인스턴스는 수정 불가
    schoolName = 'choongang'

    def method(self):
        self.num = 1 # 인스턴스가 사용할 수 있는 변수 생성
        age = 20 # 메소드 안에서만 사용할 수 있는 변수 생성

# 메소드 바깥에 있는 변수는 클래스와 인스턴스 모두 호출 가능
print(Student.schoolName) #choongang
obj = Student()
print(obj.schoolName) #choongang

# 클래스가 수정
Student.schoolName = 'megaStudy'
print('클래스로 수정한 후 출력')
print(Student.schoolName) #megaStudy
print(obj.schoolName) #megaStudy

obj.schoolName = '서울대학교'
print('인스턴스로 수정한 후 출력')
print(Student.schoolName) #megaStudy
print(obj.schoolName) #서울대학교

# 파이썬은 클래스에 없는 속성을 인스턴스에 추가 가능
obj.name = 'Park'
print(obj.name) #Park

# method에서 self.num과 age를 생성
obj.method()
print(obj.num) # 인스턴스 호출가능
print(obj.age) # age는 지역변수라서 인스턴스가 호출 불가능
#'Student' object has no attribute 'age'
'''

'''
class Student:
    
    # 생성자
    # (매개변수 없이 호출하면 name=None)
    # (매개변수를 대입하면 그 값이 name에 대입)
    def __init__(self, name = None):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name # 이 때 name이 만들어짐

obj = Student()
# 생성자가 없어도 setName을 호출하면 self.name이 만들어지기 때문에 문제가 안됨
obj.setName('park')
print(obj.getName())

obj1 = Student()
print(obj1.getName()) #생성자(__init__)가 없으면 setName을 호출하지 않았기 때문에 name이 없음
#'Student' object has no attribute 'name'
# 생성자(__init__)가 있어도 매개변수 없이 호출해서 None

obj2 = Student('Steve')
print(obj2.getName())
'''

'''

class Temp:
    # 소멸
    def __del__(self):
        print('인스턴스가 파괴됩니다.')

#  생성자를 호출해서 인스턴스를 생성한 후 t에 대입 (참조횟수1)
t = Temp()
# 인스턴스를 다른 곳에 대입하면 참조횟수가 1 증가함
k = t

import sys

print(sys.getrefcount(k))

# 변수에 None을 대입 (참조 횟수가 1 줄어듦)
t = None

del(k)  #변수를 삭제, 참조횟수가 1 줄어듦

'''

'''
class DTO:
    def __init__(self, num = 0, name = None):
        self.num = num
        self.name = name
    #name과 num 이외의 속성은 만들 수 없도록 제한
    __slots__ = ['name', 'num']

dto = DTO(1, 'park')
dto.tel = '01012538253'
'''
'''
class DTO:
    def __init__(self, name=None):
        #private처럼 클래스 외부에서는 __name에 접근할 수 없음
        self.__name = name

    def getName(self):
        print('getter')
        return self.__name
    def setName(self, name):
        print('setter')
        self.__name = name
    #.name을 호출하면 getName이 호출, .name=값을 호출하면 setName이 호출
    name = property(fget=getName, fset=setName)

        
dto = DTO('park')
#print(dto.__name) #'DTO' object has no attribute '__name'
dto.name = 'kim'
print(dto.name)
'''

li1 = [100, 300]
print(dir(li1))

li2 = [30, 70]
print(li1 + li2)  # __add__가 존재하므로 더하기 가 가능
print(li1 > li2) # __gt__ (greater than) 이 존재하므로 비교가 가능
# sub는 없어서 빼기는 불가능

