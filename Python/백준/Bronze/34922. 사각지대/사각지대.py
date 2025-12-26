from math import pi

w, h = map(int, input().split())
r = int(input())
print(w * h - (pi * (r ** 2) / 4))
