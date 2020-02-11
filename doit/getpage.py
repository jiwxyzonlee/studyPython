#getpage.py


def getTotalPage(m, n):
    if m % n ==0:
        return m//n
    else:
        return m//n + 1

tcnt = int(input("게시물 총 건수: "))
pcnt = int(input("한 페이지에 보여줄 게시물 수: "))

"""
print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))
"""

print(getTotalPage(tcnt, pcnt), "페이지")
