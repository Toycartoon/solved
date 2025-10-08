n, m, p = map(int, input().split())
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if (i + j) * 2 >= p:
            ans += (n - i + 1) * (m - j + 1)
print(ans)