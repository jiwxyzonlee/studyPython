"""
n = 1
while n <1000:
    print(n)
    n += 1

for n in range(1, 1000):
    print(n)

for n in range(1, 1000):
    if n % 3 ==0:
        print(n)

for m in range(1, 1000):
    if m % 5 ==0:
        print(m)
"""
"""
result = 0
for n in range(1, 1000):
    if n % 3 == 0:
        result += n
print(result)

result = 0
for n in range(1, 1000):
    if n % 5 == 0:
        result += n
print(result)
"""

result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)

"""
result = 0
for n in range(1, 1000):
    if n % 3 == 0 and n % 5 == 0:
        result += n
print(result)
"""
