# classBookReader02.py


class BookReader:               #클래스 BookReader 선언
    __country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):  #초기화 함수의 재정의
        self.name = name       #인스턴스 변수 name 선
    def read_book(self):       #함수 read_book 선언
        print(self.name + ' is reading a Book!!')       #출력

#reader = BookReader()                                  #인스턴스 생성
#type(reader)                                                  #변수 reader 타입 확인
#<class '__main__.BookReader'>
