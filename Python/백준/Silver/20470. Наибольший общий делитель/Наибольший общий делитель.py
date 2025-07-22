from math import gcd

n, d = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in a:
    if gcd(d, i) == d:
        b.append(i)

if len(b) == 0 or gcd(*b) != d:
    print(-1)
else:
    print(len(b))
    print(*b)
