from math import isqrt

a1, a2, a3, a4 = map(int, input().split())
print(isqrt(min(a1, a2) + min(a3, a4)))
