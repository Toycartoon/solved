n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += min(7, a[i]) - 2
    else:
        ans += min(7, a[i]) - 3

print(ans)
