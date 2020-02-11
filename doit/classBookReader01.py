# classBookReader01.py


class BookReader:               #클래스 BookReader 선언
    def __init__(self, name):  #이미 존재하는 함수 초기화(다시 정의) 함수->함수의 재정의
        self.name = name
    def read_book(self):       #함수 read_book 선언
        print(self.name + ' is reading a Book!!')       #출력

#reader = BookReader()                                  #인스턴스 생성
#type(reader)                                                  #변수 reader 타입 확인
#<class '__main__.BookReader'>
