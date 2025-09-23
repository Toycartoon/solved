from math import trunc

c, k = map(int, input().split())
d = 10 ** k
print(trunc(c / d + 0.5) * d)
