n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            if g[y][x] == "-":
                for v in range(x, m):
                    if not visited[y][v] and g[y][v] == "-":
                        visited[y][v] = True
                    else:
                        break
                ans += 1
            elif g[y][x] == "|":
                for v in range(y, n):
                    if not visited[v][x] and g[v][x] == "|":
                        visited[v][x] = True
                    else:
                        break
                ans += 1

print(ans)
