# classBookReader05.py

"""
class BookReader:               #클래스 BookReader 선언
    country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):  #초기화 함수 재정의
        self.name = name        #인스턴스 변수 name 선언  (일반변수를 객체 변수로 변경)
    def read_book(self):
        print(self.name + ' is readinig Book!!')

class Drumplayer:
    country = 'South Korea'
    def __init__(self, name):
        self.name = name
    def play_drum(self):
        print(self.name + ' is playing Drum!!')

"""
    
#두 클래스간 공통분모 뽑아서 부모 만들기

class Human:                       #부모 클래스 선언
    country = 'South Korea'   #클래스 변수 country 선언
    def __init__(self, name):   #초기화 함수 재정의
        self.name = name

class BookReader(Human):  #Human의 자식 클래스인 BookReader 클래스 선언
     def read_book(self):
         print(self.name+ ' is reading Book!!')
class DrumPlayer(Human):
    def play_drum(self):
        print(self.name + ' is playing Drum!!')
