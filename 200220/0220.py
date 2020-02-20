'''
#클래스 생성
class Student:
    #member 메소드
    def func(self):
        print('member method')

#인스턴스 생성
obj = Student()

obj.func() #인스턴스가 메소드를 호출 - 권장
Student.func(obj) #클래스가 메소드를 호출
'''

'''
class Student:
    #이 변수는 클래스와 인스턴스 모두 접근 가능하지만
    #인스턴스는 수정 못함
    schoolName = '중앙'

    def method(self):
        self.num = 1 #인스턴스가 사용할 수 있는 변수 생성
        age = 20 #메소드 안에서만 사용할 수 있는 변수 생성

#메소드 바깥에 있는 변수는 클래스와 인스턴스 모두 호출 가능
print(Student.schoolName)
obj = Student()
print(obj.schoolName)

#클래스가 수정
Student.schoolName = '메가스터디'
print('클래스로 수정 한 후 출력')
print(Student.schoolName)
print(obj.schoolName)

obj.schoolName = '서울대학교'
print('인스턴스로 수정 한 후 출력')
print(Student.schoolName)
print(obj.schoolName)

#파이썬은 클래스에 없는 속성을 인스턴스에 추가 가능
obj.name = 'Park'
print(obj.name)

#method에서 self.num 과 age를 생성
obj.method()
print(obj.num) #인스턴스가 호출가능
print(obj.age) #age는 지역변수라서 인스턴스가 호출 불가능
'''

'''
class Student:
    #생성자 - 매개변수 없이 호출하면 name=None 매개변수를 대입하면 그 값이 name에 대입
    def __init__(self, name=None):
        self.name = name
    
    def getName(self):
        return self.name


    def setName(self, name):
        self.name = name


obj = Student()
#생성자가 없어도 setName을 호출하면 self.name이 만들어지기 때문에 문제가 안됨
obj.setName('park')
print(obj.getName())

obj1 = Student()
print(obj1.getName()) #생성자가 없으면 setName을 호출하지 않았기 때문에 name이 없음

obj2 = Student('Steve')
print(obj2.getName())
'''

'''
import sys
class Temp:
    #소멸자
    def __del__(self):
        print('인스턴스가 파괴됩니다.')

#생성자를 호출해서 인스턴스를 생성한 후 t에 대입 - 참조 횟수 1
t = Temp()
#인스턴스를 다른 곳에 대입하면 참조 횟수가 1증가 합니다.
k = t

print(sys.getrefcount(k))

#변수에 None을 대입 - 참조 횟수가 1줄어듬
t = None

del(k) #변수를 삭제합니다. 참조횟수가 1줄어듬
'''

'''
class DTO:
    def __init__(self, num=0, name=None):
        self.num = num
        self.name = name
    #name 과 num 이외의 속성은 만들 수 없도록 제한하기
    __slots__ = ['name', 'num']

dto = DTO(1, 'park')
dto.tel = '0103790199'
'''

'''
class DTO:
    def __init__(self, name=None):
        #private 처럼 클래스 외부에서는 __name에 접근할 수 없습니다.
        self.__name = name

    def getName(self):
        print('getter')
        return self.__name
    def setName(self, name):
        print('setter')
        self.__name = name

    #.name을 호출하면 getName이 호출되고 .name=값 을 호출하면 setName이 호출 
    name = property(fget=getName, fset=setName)

dto = DTO('park')
#print(dto.__name)
dto.name = 'kkk'
print(dto.name)
'''

li1 = [100, 300]
#print(dir(li1))
li2 = [30, 70]
print(li1 + li2) #__add__ 가 있어서 더하기 가능
print(li1 > li2) #__gt__ 가 있어서 > 가능 











    
