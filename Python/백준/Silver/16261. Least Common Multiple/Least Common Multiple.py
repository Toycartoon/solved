from math import gcd, lcm

for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    temp = lcm(b, d)
    a *= temp // b
    c *= temp // d

    i = lcm(a, c)
    print(i // gcd(i, temp), temp // gcd(i, temp))
