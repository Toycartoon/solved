n = int(input())
a = list(map(int, input().split()))

ans = 0
a.sort(reverse=True)
for i in range(n // 2):
    ans += a[i]
print(ans)
