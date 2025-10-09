from math import inf

a, b, n = map(int, input().split())
ans = inf
for i in range(n):
    c, _ = map(int, input().split())
    v = list(map(int, input().split()))
    if a in v and b in v and v.index(a) < v.index(b):
        ans = min(ans, c)
print(ans if ans != inf else -1)
