n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 1
for i in range(1, n):
    if a[i-1] + a[i] <= x:
        ans += 1
    else:
        break
print(ans)
