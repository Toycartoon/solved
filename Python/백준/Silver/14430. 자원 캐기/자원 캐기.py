import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for __ in range(n)]

for y in range(n):
    for x in range(m):
        dp[y][x] = max(dp[y-1][x] if y > 0 else 0, dp[y][x-1] if x > 0 else 0) + g[y][x]

print(dp[-1][-1])
