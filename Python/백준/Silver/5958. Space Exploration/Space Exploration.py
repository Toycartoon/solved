from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    q.append((_x, _y))
    pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                if g[y+dy][x+dx] == "*" and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))

n = int(input())
g = [[*input().strip()] for _ in range(n)]
visited = [[False] * n for _ in range(n)]

ans = 0
for y in range(n):
    for x in range(n):
        if g[y][x] == "*" and not visited[y][x]:
            bfs(x, y)
            ans += 1
print(ans)
