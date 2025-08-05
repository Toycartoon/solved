n = int(input())
a = list(map(int, input().split()))

ans = 0
x = 1
for i in range(1, n):
    if a[i-1] <= a[i]:
        x += 1
    else:
        ans = max(ans, x)
        x = 1

ans = max(ans, x)
print(ans)
