# classBookReader.py


class BookReader:                                         #클래스 BookReader 선언
    name = str()                                             #문자열 타입 변수 name 선언
    def read_book(self):                                       #함수 read_book 선언
        print(self.name + ' is reading a Book!!')       #출력

reader = BookReader()                                  #인스턴스 생성
type(reader)                                                  #변수 reader 타입 확인
#<class '__main__.BookReader'>
