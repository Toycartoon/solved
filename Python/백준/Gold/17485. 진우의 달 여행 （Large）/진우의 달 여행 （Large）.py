from math import inf

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

dp = [[[inf, inf, inf] for _ in range(m)] for __ in range(n)]
for i in range(m):
    dp[0][i] = [g[0][i]] * 3

for i in range(1, n):
    for j in range(m):
        if j != 0:
            dp[i][j][0] = g[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
        if j != m-1:
            dp[i][j][2] = g[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])
        dp[i][j][1] = g[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])

ans = []
for i in range(m):
    ans.extend(dp[-1][i])
print(min(ans))
