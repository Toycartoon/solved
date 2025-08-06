import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [input().strip().split() for _ in range(n)]

a = 0
for y in range(n):
    for x in range(m):
        a += g[y][x].count("9")

mx = 0
for i in g:
    mx = max(mx, "".join(i).count("9"))

for i in zip(*g):
    mx = max(mx, "".join(i).count("9"))

print(a - mx)
