import sys

input = sys.stdin.readline

n, m = map(int, input().split())
w = {}
for i in range(n):
    a, b = input().strip().split()
    w[a] = int(b)

ans = 0
for i in range(m):
    c, d = input().strip().split()
    if w[c] * 1.05 < int(d):
        ans += 1

print(ans)
