score = int(input("Enter your score here: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade =  'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score, 'is followed by', grade)

print("%d is followed by %c"%(score,grade))
