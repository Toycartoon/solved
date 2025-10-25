from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    q.append((_x, _y))
    visited[_y][_x] = True
    pos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    c = 1
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < m and 0 <= y + dy < n:
                if g[y+dy][x+dx] == 1 and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))
                    c += 1
    return c

n, m = map(int, input().split())
g = [list(map(int, [*input().strip()])) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = []
for y in range(n):
    for x in range(m):
        if g[y][x] == 1 and not visited[y][x]:
            ans.append(bfs(x, y))
ans.sort()

print(len(ans))
print(*ans)
