#emp01.py

class payment:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def rise(self):
        result = self.pay * 1.1
        return result

fullName = input('이름을 입력하세요: ')
salary = int(input('기존 연봉을 입력하세요: '))

amt = payment(fullName, salary)
new_amt = amt.rise()

print('%s님의 내년 연봉은 %d 만원입니다.' %(fullName, new_amt))


"""
궁금쓰

if __ name__ == "__main__":
    fullName = input('이름을 입력하세요: ')
    salary = int(input('기존 연봉을 입력하세요: '))
    amt = payment(fullName, salary)
    new_amt = amt.rise()
    print('%s님의 내년 연봉은 %d 만원입니다.' %(fullName, new_amt))
"""
