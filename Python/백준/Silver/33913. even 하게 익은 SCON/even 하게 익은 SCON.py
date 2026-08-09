n = int(input())
dp = [[0, 0] for _ in range(n+1)]   # E(lse), SC

dp[0][0] = 1
for i in range(1, n+1):
    dp[i][0] = (dp[i-1][0] * 24 + dp[i-1][1] * 2) % 1000000007
    dp[i][1] = (dp[i-1][0] * 2 + dp[i-1][1] * 24) % 1000000007

print(dp[-1][0] % 1000000007)
