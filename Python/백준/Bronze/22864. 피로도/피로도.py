a, b, c, m = map(int, input().split())
ans = 0
p = 0
for i in range(24):
    if a + p <= m:
        ans += b
        p += a
    else:
        p = max(p-c, 0)
print(ans)
