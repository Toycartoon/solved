n = int(input())

ans = (11, 11)
for i in range(1, 11):
    for j in range(1, 11):
        if i * j >= n:
            if i + j < ans[0] + ans[1]:
                ans = (i, j)

print(*ans)
