from math import gcd, lcm

x, y = map(int, input().split())
if x == y:
    print(0)
elif gcd(x, y) != 1:
    print(1)
    print(y-x)
else:
    print(2)
    print(lcm(x, y)-x)
    print(y-lcm(x, y))
