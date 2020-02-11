#classBird

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):       #overriding
        print('very fast')
eagle = Eagle()
eagle.fly()
