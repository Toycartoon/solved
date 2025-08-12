from math import pi

d, h = map(float, input().split())
r = d / 2 + 5
print(2 * pi * r * h + pi * r ** 2)
