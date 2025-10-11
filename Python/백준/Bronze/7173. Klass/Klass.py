m, n = map(int, input().split())
g = [[*input()] for _ in range(m)]

ans = 0
pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for y in range(m):
    for x in range(n):
        s = 0
        d = 0
        for dx, dy in pos:
            if 0 <= y+dy < m and 0 <= x+dx < n:
                d += 1
                s += abs(int(g[y][x]) - int(g[y+dy][x+dx]))
        ans += s / d
print(f"{ans:.04f}")
