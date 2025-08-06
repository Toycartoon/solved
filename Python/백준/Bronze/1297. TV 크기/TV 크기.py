from math import trunc

d, h, w = map(int, input().split())
b = h * d / ((w ** 2 + h ** 2) ** 0.5)
a = b * w / h
print(trunc(b), trunc(a))
