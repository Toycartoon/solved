from collections import deque

q = deque()
def bfs(_x, _y):
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited[_y][_x] = True
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == "*":
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))


n, m = map(int, input().split())
g = [[*input()] for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]

ans = 0
for y in range(n):
    for x in range(m):
        if g[y][x] == "*" and not visited[y][x]:
            bfs(x, y)
            ans += 1
print(ans)
