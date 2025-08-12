from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

q = deque()
def bfs(_x):
    visited[_x] = 0
    q.append(_x)

    while q:
        x = q.popleft()

        for i in g[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                q.append(i)

bfs(x)
ans = []
for i in range(n+1):
    if visited[i] == k:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
