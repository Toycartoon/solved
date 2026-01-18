from math import gcd

a, b = map(int, input().split())
if a == b:
    print("INF")
else:
    g = gcd(min(a, b) ** 2, max(a, b)-min(a, b))
    print((min(a, b) ** 2) // g, (max(a, b)-min(a, b)) // g)