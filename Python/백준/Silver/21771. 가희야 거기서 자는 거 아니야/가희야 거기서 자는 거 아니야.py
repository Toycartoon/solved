r, c = map(int, input().split())
rg, cg, rp, cp = map(int, input().split())
g = [input() for _ in range(r)]

p = rp * cp
s = 0
for y in range(r):
    s += g[y].count("P")

print(int(s != p))
