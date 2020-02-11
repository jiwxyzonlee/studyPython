#classFamily.py

class Family:
    lastname = '김'


print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)


# 클래스 변수 변경

Family.lastname = '박'
print(a.lastname)
print(b.lastname)
