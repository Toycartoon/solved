n, m = map(int, input().split())
v = []
for i in range(m):
    a, b = map(int, input().split())
    v.append((a, b))

v.sort(key=lambda x: (-x[0]))
ans = 0
for i in range(m-1):
    if v[i][0] >= n:
        continue
    else:
        ans += n-v[i][0]
print(ans)
