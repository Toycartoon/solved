x, k = map(int, input().split())
a = list(map(int, input().split()))

l = [0 for _ in range(k+1)]
r = [0 for _ in range(k+1)]
for i in range(2 * x):
    if i < x:
        l[a[i]] += 1
    else:
        r[a[i]] += 1

ans = 0
for i in range(1, k+1):
    ans += l[i] * (x - r[i])

print(ans)
