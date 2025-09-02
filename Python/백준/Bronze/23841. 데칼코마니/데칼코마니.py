n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]

for y in range(n):
    for x in range(m):
        if g[y][x] != ".":
            g[y][-x-1] = g[y][x]

for v in g:
    print("".join(v))
