from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    q.append((_x, _y))
    pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    c = 0
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if g[y+dy][x+dx] == "*" and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    c += 1
    return c


n, m = map(int, input().split())
g = [[*input().strip()] for _ in range(m)]
visited = [[False] * n for _ in range(m)]

ans = []
for y in range(m):
    for x in range(n):
        if g[y][x] == "*" and not visited[y][x]:
            ans.append(bfs(x, y))
print(max(ans))
