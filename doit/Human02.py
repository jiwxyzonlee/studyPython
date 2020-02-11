# Human02.py

"""
class BookReader:               #클래스 BookReader 선언
    country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):  #초기화 함수 재정의
        self.name = name        #인스턴스 변수 name 선언  (일반변수를 객체 변수로 변경)
    def read_book(self):
        print(self.name + ' is readinig a Book!!')

class Drumplayer:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def play_drum(self):
        print(self.name + ' is playing a Drum!!')

"""
    
#두 클래스간 공통분모 뽑아서 부모 만들기

class Human:                       #부모 클래스 선언
    country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):   #초기화 함수 재정의
        self.name = name
    def eat_meal(self):
        print(self.name + ' is eating meal!!')

class BookReader(Human):  #Human의 자식 클래스인 BookReader 클래스 선언
     def read_book(self):
         print(self.name+ ' is reading a Book!!')
class DrumPlayer(Human):
    def play_drum(self):
        print(self.name + ' is playing a Drum!!')


#새 자식 클래스 추가

class BookWriter(Human):   #Human의 자식 클래스인 BookWriter 클래스 선언
    def write_book(self):
        print(self.name + ' is writing a Book!!')

"""
<책을 쓰는 사람은 컴퓨터 프로그래밍 관련 책만 집필한다는 것으로 가정>
<'개발자' Developer class 생성한뒤 책 쓰는 사람과 관계 맺기>
"""


class Developer:         #Developer 부모 클래스 선언
    def coding(self):    #coding 메소드 선언
        print(self.name + ' is a developer!!')
class ProgramBookWriter(Human, Developer):
    def write_book(self):
        print(self.name + ' is writing a book!!')

"""
개발자를 부모 클래스로 하고, 파이썬 개발자, 자바 개발자, C++개발자의 세 개의 자식 클래스로 나누기
"""

class Developer:         #Developer 부모 클래스 선언
    def __init__(self, name):   #초기화 시 name을 받기 위한 재정의
        self.name = name
    def coding(self):    #coding 메소드 선언
        print(self.name + ' is a developer!!')

class PythonDeveloper(Developer):   #PythonDeveloper 자식 클래스 선언
    def coding(self):    #coding 메소드 선언
        print(self.name + ' is a Python developer!!')
class JavaDeveloper(Developer):   #JavaDeveloper 자식 클래스 선언
    def coding(self):        #coding 메소드 선언
        print(self.name + ' is a Java developer!!')
class CPPDeveloper(Developer):  #CPPDeveloper 자식 클래스 선언
    def coding(self):       #coding 메소드 선언
        print(self.name + ' is a C++ developer!!')

class CPPDeveloper(Developer):
    def coding(self):
        super().coding()
        print(self.name + ' is a C++ developer!!')
