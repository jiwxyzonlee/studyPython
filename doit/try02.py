try:

    a = [1, 2]

    print(a[3])

    4/0

except (ZeroDivisionError, IndexError) as e and r:

    print(e)
    print(r)
