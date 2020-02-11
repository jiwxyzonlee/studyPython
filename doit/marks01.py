marks = [90, 25, 67, 45, 80]


#variables
number = 0

for mark in marks:
    number = number + 1
    if mark >= 60:
        print("{0}번 학생은 {1}점이므로  합격입니다." .format(number, mark))
        #print("%d번 학생은 %d점이므로 합격입니다." %(number, mark))
    else:
        print("{0}번 학생은 {1}점이므로 불합격입니다." .format(number, mark))
        #print("%d번 학생은 %d점이므로 불합격입니다." %(number, mark))
