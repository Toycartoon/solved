import sys

input = sys.stdin.readline

n = int(input())
g = [int(input()) for _ in range(n)]

ans = 0
for i in range(n // 2):
    if g[i] == g[i + n // 2]:
        ans += 1

print(ans * 2)
