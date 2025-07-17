from math import inf

n, m = map(int, input().split())

s = 0
mn = inf
for i in range(n):
    a = list(map(int, input().split()))

    s += sum(a)
    mn = min(mn, min(a))

print(s - mn)
