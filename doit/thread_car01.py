#thread_car01,py

import time

##클래스 선언부분
class RacingCar:
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for i in range(0,5):
            carStr = self.carName + '~%d번 달립니다.' % (i + 1)
            print(carStr)
            time.sleep(0.1)

#메인코드 부분

car1 = RacingCar('H자동차')
car2 = RacingCar('K자동차')
car3 = RacingCar('D자동차')

car1.runCar()
print()
car2.runCar()
print()
car3.runCar()
