import sys
from collections import deque
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))
g = [{} for _ in range(n+1)]
visited = [(0, inf, 0) for _ in range(n+1)]

q = deque()
def bfs(_x):
    q.append(_x)

    while q:
        x = q.popleft()

        for v in g[x]:
            if not visited[v][0] or (visited[x][0] + 1 == visited[v][0] and (visited[v][1] > (visited[x][1] + g[x][v][0]) or visited[v][2] < visited[x][2] + g[x][v][1])):
                if not visited[v][0]:
                    q.append(v)
                visited[v] = (visited[x][0] + 1, min(visited[v][1], (visited[x][1] + g[x][v][0]) if visited[x][1] != inf else g[x][v][0]), max(visited[v][2], visited[x][2] + g[x][v][1]))


for i in range(m):
    v, w, f = map(int, input().split())
    tmp = f+(t[w-2] if w != 1 else 0)
    if w in g[v]:
        g[v][w] = (min(tmp, g[v][w][0]), max(tmp, g[v][w][1]))
    else:
        g[v][w] = (tmp, tmp)

bfs(1)
print(visited[1][1] if visited[1][1] != inf else 0)
print(visited[1][2])
