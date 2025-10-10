import sys

input = sys.stdin.readline

h, x = map(int, input().split())
c = []
for i in range(h):
    c.append(int(input()))

ans = 0
for i in range(h):
    ans += c[i] * pow(x, i+1, 1000000007)
    ans %= 1000000007
print(ans)
