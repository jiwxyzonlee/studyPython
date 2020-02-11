marks = [90, 25, 67, 45, 80]


#variables
number = 0

for mark in marks:
    number = number + 1
    if mark  < 60:
        continue
    print("%d번 학생은 %d점이므로 합격입니다." %(number, mark))
