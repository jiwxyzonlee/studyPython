# classBookReader04.py


class BookReader:               #클래스 BookReader 선언
    country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):  #초기화 함수 재정의
        self.name = name        #인스턴스 변수 name 선언(일반변수를 객체 변수로 변경)
    def read_book(self):
        print(self.name + ' is readinig Book!!')

class Drumplayer:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def play_drum(self):
        print(self.name + ' is playing Drum!!')
    
