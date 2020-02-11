score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("%d점은 %c학점입니다" % (score, grade))
