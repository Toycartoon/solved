n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for __ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(2, n):
        for k in range(3):
            if k == 0:
                if a[i][j] == 0:
                    dp[i][j][k] = dp[i][j-1][0] + dp[i][j-1][1]
            elif k == 1:
                if i > 0 and a[i][j] == a[i-1][j] == a[i][j-1] == 0:
                    dp[i][j][k] = sum(dp[i-1][j-1])
            elif k == 2:
                if i > 0 and a[i][j] == 0:
                    dp[i][j][k] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[-1][-1]))
