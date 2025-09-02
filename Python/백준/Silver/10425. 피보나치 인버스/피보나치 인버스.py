import sys

input = sys.stdin.readline

dp = [0, 1]
for i in range(2, 100001):
    dp.append(dp[-1] + dp[-2])

for t in range(int(input())):
    n = int(input())
    l, r = -1, 100001
    while l+1 < r:
        mid = (l + r) // 2
        if dp[mid] > n:
            r = mid
        else:
            l = mid
    print(l)
