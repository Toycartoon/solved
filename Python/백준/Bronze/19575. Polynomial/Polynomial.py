import sys

input = sys.stdin.readline

n, x = map(int, input().split())
ans = 0
for _ in range(n+1):
    a, i = map(int, input().split())
    ans += a * pow(x, i, 1000000007)
    ans %= 1000000007
print(ans)
