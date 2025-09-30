from collections import deque

q = deque()
def bfs(_x, _y):
    pos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited[_y][_x] = True
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < c and 0 <= y+dy < r:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == "#":
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))

r, c = map(int, input().split())
g = [[*input()] for _ in range(r)]
visited = [[False for _ in range(c)] for __ in range(r)]

ans = 0
for y in range(r):
    for x in range(c):
        if g[y][x] == "#" and not visited[y][x]:
            bfs(x, y)
            ans += 1
print(ans)
