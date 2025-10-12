n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()

ans = 0
for i in range(n-k):
    ans += a[i]
print(ans)
