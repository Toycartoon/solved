n = int(input())
a = list(map(int, input().split()))

ans = n-2 if a[0] != 1 else n-1
for i in range(1, n):
    if a[i] != i+1:
        ans = (ans * (n-2)) % 998244353
    else:
        ans = (ans * (n-1)) % 998244353
print(ans % 998244353)
