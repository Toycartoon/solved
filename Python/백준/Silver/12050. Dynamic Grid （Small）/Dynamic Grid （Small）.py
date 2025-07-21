from collections import deque
import sys

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    visited[_y][_x] = True
    pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q.append((_x, _y))
    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if 0 <= x+dx < c and 0 <= y+dy < r:
                if g[y+dy][x+dx] == "1" and not visited[y+dy][x+dx]:
                    visited[y+dy][x+dx] = True
                    q.append((x+dx, y+dy))


for t in range(int(input())):
    r, c = map(int, input().split())
    g = [[*input().strip()] for _ in range(r)]

    print(f"Case #{t+1}:")
    for i in range(int(input())):
        com, *xyz = input().strip().split()

        if com == "M":
            x, y, z = map(int, xyz)
            g[x][y] = str(z)
        elif com == "Q":
            ans = 0
            visited = [[False for _ in range(c)] for __ in range(r)]
            for y in range(r):
                for x in range(c):
                    if g[y][x] == "1" and not visited[y][x]:
                        bfs(x, y)
                        ans += 1

            print(ans)
