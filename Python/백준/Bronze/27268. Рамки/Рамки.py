h, w, n = map(int, input().split())
g = [["." for _ in range(w)] for __ in range(h)]

for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    for y in range(r1-1, r2):
        g[y][c1-1] = chr(97+i)
        g[y][c2-1] = chr(97+i)

    for x in range(c1-1, c2):
        g[r1-1][x] = chr(97+i)
        g[r2-1][x] = chr(97+i)

for i in g:
    print(*i, sep="")
