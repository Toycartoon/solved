n = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(1, n+1):
    if a[i] > 1 and not (a[i-1] == 1 and i == 1):
        ans *= a[i]
    else:
        ans += a[i]
    ans %= (10 ** 9 + 7)
print(ans)
