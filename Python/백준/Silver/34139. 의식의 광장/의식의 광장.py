import sys

input = sys.stdin.readline

h, n = map(int, input().split())
a = []
for i in range(n):
    r, c = map(int, input().split())
    a.append((r, c, i))

a.sort(key=lambda x: (-x[1], -x[0]))
ans = [0 for _ in range(n)]

x = n
for r, c, v in a:
    ans[v] = x
    x -= 1

print("YES")
print(*ans)
