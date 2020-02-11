# classBookReader03.py


class BookReader:               #클래스 BookReader 선언
    __country = 'South Korea'   #클래스 변수 country 선언
    def update_country(self, country): #변경 method 선언
        self.__country = country   #country값 변경
    def get_country(self):      #country 값 반환 method 선언
        return self.__country     #country 값 반환
