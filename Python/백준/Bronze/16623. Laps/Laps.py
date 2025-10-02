n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, m):
    if a[i-1] > a[i]:
        ans += 1
print(ans)
