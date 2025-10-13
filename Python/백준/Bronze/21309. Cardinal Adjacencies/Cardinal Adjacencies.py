n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

edge, vertex = 0, 0
for y in range(n):
    for x in range(m):
        if g[y][x] != 1:
            continue

        if x > 0 and y > 0 and g[y-1][x-1] == 1:
            vertex += 1
        if x > 0 and y < n-1 and g[y+1][x-1] == 1:
            vertex += 1
        if x < m-1 and y > 0 and g[y-1][x+1] == 1:
            vertex += 1
        if x < m-1 and y < n-1 and g[y+1][x+1] == 1:
            vertex += 1
        if x > 0 and g[y][x-1] == 1:
            edge += 1
        if x < m-1 and g[y][x+1] == 1:
            edge += 1
        if y > 0 and g[y-1][x] == 1:
            edge += 1
        if y < n-1 and g[y+1][x] == 1:
            edge += 1
print(edge // 2, (vertex+edge) // 2)
