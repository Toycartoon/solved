from math import gcd

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    g = gcd(a, b)
    print((a // g) * (b // g))
