a, b = 0, 0
c, d = 0, 0
for i in range(int(input())):
    e, v1, v2 = map(int, input().split())
    c += v1
    d += v2
    if v1 > v2:
        a += e
    elif v2 > v1:
        b += e

if a > b and c > d:
    print(1)
elif b > a and d > c:
    print(2)
else:
    print(0)
