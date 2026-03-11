n = int(input())
g = [input() for _ in range(n)]
visited = [[False for _ in range(__ + 1)] for __ in range(n)]

f = True
for y in range(n):
    for x in range(len(visited[y])):
        if not visited[y][x]:
            try:
                if g[y][x] == "R":
                    if g[y+1][x] == g[y+1][x+1] == "R" and not (visited[y+1][x] or visited[y+1][x+1]):
                        visited[y+1][x] = True
                        visited[y+1][x+1] = True
                    else:
                        f = False
                        break
                elif g[y][x] == "B":
                    if g[y][x+1] == g[y+1][x+1] == "B" and not (visited[y][x+1] or visited[y+1][x+1]):
                        visited[y][x+1] = True
                        visited[y+1][x+1] = True
                    else:
                        f = False
                        break
            except IndexError:
                f = False
                break
print(int(f))
