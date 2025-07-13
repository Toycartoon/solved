import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
g = set()

b = 0
x = 0
for i in range(n):
    y = int(input())

    if b >= y:
        x += 1

    g.add((x, y))
    b = y

q = deque()
pos = [(0, 1), (1, 0), (-1, 0), (0, -1)]
def bfs(_x, _y):
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            if (x+dx, y+dy) in g:
                g.remove((x+dx, y+dy))
                q.append((x+dx, y+dy))

ans = 0
while g:
    x, y = g.pop()
    ans += 1
    bfs(x, y)

print(ans)
print(n)
