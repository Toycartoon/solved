g = [[*input()] for _ in range(8)]
visited = [[False for _ in range(8)] for _ in range(8)]

for y in range(8):
    for x in range(8):
        if g[y][x] == "R":
            for r in range(8):
                visited[r][x] = True
            for c in range(8):
                visited[y][c] = True

ans = 0
for y in range(8):
    for x in range(8):
        if not visited[y][x]:
            ans += 1
print(ans)
