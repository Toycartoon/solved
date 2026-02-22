n, m = map(int, input().split())
dp = [[0 for _ in range(n)] for __ in range(m)]

dp[0][0] = 1
for i in range(m):
    for j in range(n):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        if i > 0 and j > 0:
            dp[i][j] += dp[i-1][j-1]
        dp[i][j] %= 1000000007
print(dp[-1][-1])
