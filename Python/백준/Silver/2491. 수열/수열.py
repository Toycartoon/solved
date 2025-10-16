n = int(input())
a = list(map(int, input().split()))

ans = 0
v = 1
for i in range(1, n):
    if a[i-1] <= a[i]:
        v += 1
    else:
        ans = max(ans, v)
        v = 1
ans = max(ans, v)

v = 1
for i in range(1, n):
    if a[i-1] >= a[i]:
        v += 1
    else:
        ans = max(ans, v)
        v = 1
print(max(ans, v))
