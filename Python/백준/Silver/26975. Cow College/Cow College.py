n = int(input())
a = list(map(int, input().split()))

ans = (0, 0)
a.sort()
for i in range(n):
    if ans[0] < a[i] * (n-i):
        ans = (a[i] * (n-i), a[i])
print(*ans)
