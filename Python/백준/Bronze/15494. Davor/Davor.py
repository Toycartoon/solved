n = int(input())
ans = (0, 0)
for x in range(1, 101):
    for k in range(1, 101):
        if (7 * x + 21 * k) * 52 == n:
            ans = max(ans, (x, k))
print(ans[0])
print(ans[1])
