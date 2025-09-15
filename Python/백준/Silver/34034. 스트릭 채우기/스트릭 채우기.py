n, m, k = map(int, input().split())
d = list(enumerate(map(int, input().split())))

d.sort(key=lambda x: x[1])
v = []
for i in range(n):
    if d[i][1]-1 <= m:
        m -= d[i][1]-1
        v.extend([0] * (d[i][1]-1) + [d[i][0]+1])
    else:
        break

v.extend([0] * m)
if len(v) < k:
    print(-1)
else:
    print(*v[:k])
