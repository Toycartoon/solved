from math import ceil

n, m = map(int, input().split())
t, s = map(int, input().split())

z = (ceil(n / 8) - 1) * s + n
d = t + (ceil(m / 8) - 1) * (s + 2 * t) + m
if z > d:
    print("Dok")
    print(d)
else:
    print("Zip")
    print(z)
