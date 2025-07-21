n, d, k = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
a = [0 for _ in range(n)]
for i in range(d):
    for x in range(n):
        a[x] += s[x]

    if max(a) > k:
        ans += 1
        a = [*s]

print(ans)
