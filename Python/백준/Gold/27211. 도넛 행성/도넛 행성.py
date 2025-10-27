from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    q.append((_x, _y))
    visited[_y][_x] = True
    pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if g[(y+dy)%n][(x+dx)%m] == 0 and not visited[(y+dy)%n][(x+dx)%m]:
                visited[(y+dy)%n][(x+dx)%m] = True
                q.append(((x+dx)%m, (y+dy)%n))


n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if g[y][x] == 0 and not visited[y][x]:
            bfs(x, y)
            ans += 1
print(ans)
