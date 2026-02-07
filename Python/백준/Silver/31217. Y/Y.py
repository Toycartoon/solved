import sys
from math import comb

input = sys.stdin.readline

n, m = map(int, input().split())
g = [0 for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    g[u-1] += 1
    g[v-1] += 1

ans = 0
for i in range(n):
    ans += comb(g[i], 3) % (10 ** 9 + 7)
print(ans % (10 ** 9 + 7))
