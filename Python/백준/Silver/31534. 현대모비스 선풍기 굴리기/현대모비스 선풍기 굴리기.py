from math import pi

a, b, h = map(int, input().split())

if a == b:
    print(-1)
    exit()

if a > b:
    b, a = a, b

d = b * h / (b - a)
print(((b ** 2 + d ** 2) - (a ** 2 + (d-h) ** 2)) * pi)
