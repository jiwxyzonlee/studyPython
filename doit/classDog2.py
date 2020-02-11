# classDog2.py

class Dog:
    #tricks = []                       #클래스 변수(인스턴스 간 공유)
    def __init__(self, name):
        self.name = name
        self.tricks = []              #인스턴스 변수 선언
    def add_trick(self, trick):
        self.tricks.append(trick) #클래스 변수 값 추가
