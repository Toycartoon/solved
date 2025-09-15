n, m, l = map(int, input().split())
a = [0 for _ in range(n)]

a[1] = 1
i = 1
ans = 0
while a[i] < m:
    if a[i] % 2 == 1:
        i = (i + l) % n
    else:
        i = (i - l) % n
    a[i] += 1
    ans += 1

print(ans)
