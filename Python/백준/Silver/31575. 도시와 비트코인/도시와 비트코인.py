from collections import deque

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
visited = [[False for _ in range(n)] for __ in range(m)]

q = deque()
def bfs(_x, _y):
    visited[_y][_x] = True
    q.append((_x, _y))

    pos = [(0, 1), (1, 0)]
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if not visited[y+dy][x+dx] and g[y+dy][x+dx] == 1:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))

    return visited[-1][-1]

print("Yes" if bfs(0, 0) else "No")
