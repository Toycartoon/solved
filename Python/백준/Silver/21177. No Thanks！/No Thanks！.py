n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = a[0]
for i in range(1, n):
    if a[i-1]+1 != a[i]:
        ans += a[i]
print(ans)
