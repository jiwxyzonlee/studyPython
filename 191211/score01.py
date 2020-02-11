# C:/doip/score01.py
score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        if score >= 70:
            grade = "C"
        else:
            if score >= 60:
                grade = "D"
            else:
                grade = "F"

print("%d점은 %c학점입니다" % (score, grade))
