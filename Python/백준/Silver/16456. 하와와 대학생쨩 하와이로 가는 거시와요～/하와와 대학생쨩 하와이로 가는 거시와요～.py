n = int(input())
dp = [0 for _ in range(n+1)]
for i in range(min(n, 3)+1):
    dp[i] = 1

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-3]) % 1000000009

print(dp[-1])
