import sys

input = sys.stdin.readline

n = int(input())
u = int(input())
ans = 0
for i in range(n-1):
    v = int(input())
    ans += max(u, v)
    u = v
print(ans)
