n = int(input())
ans = 0
for i in range(1, n // 3 + 1):
    for j in range(1, n // 3 + 1):
        if (3 * (i + j) + (n - (3 * (i + j)))) == n and (n - (3 * (i + j))) % 3 == 0 and (n - (3 * (i + j))) > 0:
            ans += 1
print(ans)
