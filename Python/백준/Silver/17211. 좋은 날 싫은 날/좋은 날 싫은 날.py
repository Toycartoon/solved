from decimal import Decimal as d
from math import trunc

n, feel = map(int, input().split())
hh, hb, bh, bb = input().split()

dp = [[d("0"), d("0")] for _ in range(n+1)]
dp[0][feel] += d("1")
for i in range(1, n+1):
    dp[i][0] = dp[i-1][1] * d(bh) + dp[i-1][0] * d(hh)
    dp[i][1] = dp[i-1][0] * d(hb) + dp[i-1][1] * d(bb)

print(trunc(dp[-1][0] * 1000 + d("0.5")))
print(trunc(dp[-1][1] * 1000 + d("0.5")))
