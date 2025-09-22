n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 1
v = x[0]
for i in x:
    if i - v > k:
        ans += 1
        v = i
print(ans)
