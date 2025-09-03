from math import gcd

a, b = map(int, input().split())
g = gcd(a, b)
for i in range(1, g+1):
    if g % i != 0:
        continue
    print(i, a // i, b // i)
