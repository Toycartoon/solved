from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y, color, k):
    g[_y][_x] = k
    q.append((_x, _y))
    pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < c and 0 <= y + dy < r:
                if g[y+dy][x+dx] == color and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    g[y+dy][x+dx] = k
                    q.append((x+dx, y+dy))

                    
r, c = map(int, input().split())
g = [[*input().strip()] for _ in range(r)]
visited = [[False] * c for _ in range(r)]
y, x, k = map(int, input().split())

bfs(x, y, g[y][x], k)
for v in g:
    print(*v, sep="")
