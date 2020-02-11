

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

"""

try:
    f = open('나 없는 파일', 'r')
except FileNotFoundError:
    pass
"""
