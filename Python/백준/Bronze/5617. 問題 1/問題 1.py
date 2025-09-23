triangle, acute, right, obtuse = 0, 0, 0, 0
while True:
    v = list(map(int, input().split()))
    a, b, c = sorted(v)
    if not (a < b + c and b < a + c and c < a + b):
        print(triangle, right, acute, obtuse)
        break

    triangle += 1
    if a ** 2 + b ** 2 > c ** 2:
        acute += 1
    elif a ** 2 + b ** 2 < c ** 2:
        obtuse += 1
    else:
        right += 1
