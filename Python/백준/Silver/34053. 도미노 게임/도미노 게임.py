from math import inf

n, m = map(int, input().split())

s = 0
z = False
mn = inf
for i in range(n):
    a = list(map(int, input().split()))
    if 0 in a:
        z = True

    s += sum(a)
    mn = min(mn, min(a))

if z:
    print(s)
else:
    print(s - mn)
