n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
for i in range(n if n % 2 == 1 else n-1):
    if a[i] % 2 == 1:
        ans += a[i]
    else:
        ans += a[i]-1
print(ans)
