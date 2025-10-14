n, m = map(int, input().split())
g = [input() for _ in range(n)]

a = [["." for _ in range(m)] for __ in range(n)]
for y in range(n):
    for x in range(m):
        if g[y][x] == "#":
            a[y][x] = "#"
            a[y+1][x] = "#"
            a[y][x+1] = "#"
            a[y+1][x+1] = "#"

for i in a:
    print(*i, sep="")
