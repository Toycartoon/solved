n, k = map(int, input().split())
a = []
for i in range(n):
    d, t = map(int, input().split())
    a.append((d, t))
a.sort(reverse=True)

ans = 0
t = float('inf')
for i in range(k):
    ans += a[i][0]
    t = min(t, a[i][1])
print(ans, t)
