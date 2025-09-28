from math import ceil

n, k, m = map(int, input().split())
a = []
for i in range(k):
    v, *g = map(int, input().split())
    a.append(g)
d = list(map(int, input().split()))

ans = 0
for i in range(k):
    s = 0
    for v in a[i]:
        s += d[v-1]
    ans += ceil(s / m)
print(ans)
