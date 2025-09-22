from collections import deque

q = deque()
def bfs(_x, _y):
    pos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
    visited[_y][_x] = 0
    q.append((_x, _y))
    while q:
        x, y = q.popleft()
        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if visited[y+dy][x+dx] == -1 and g[y+dy][x+dx] != "#":
                    visited[y+dy][x+dx] = visited[y][x] + 1
                    q.append((x+dx, y+dy))


n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]
visited = [[-1 for _ in range(m)] for __ in range(n)]
nx, ny = -1, -1
ex, ey = -1, -1
for u in range(n):
    for v in range(m):
        if g[u][v] == "K":
            nx, ny = v, u
        elif g[u][v] == "X":
            ex, ey = v, u

bfs(nx, ny)
print(visited[ey][ex])
