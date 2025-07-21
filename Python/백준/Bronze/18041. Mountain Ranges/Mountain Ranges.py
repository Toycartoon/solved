n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
x = 1
for i in range(1, n):
    if a[i]-a[i-1] > m:
        ans.append(x)
        x = 1
    else:
        x += 1

ans.append(x)
print(max(ans))
