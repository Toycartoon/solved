import sys
from collections import deque

input = sys.stdin.readline

q = deque()
def bfs(x):
    q.append(x)
    visited[x] = 0

    while q:
        v = q.popleft()
        for i in g[v]:
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)

    return visited

def backtrack(x):
    q.append(x)

    while q:
        v = q.popleft()
        for i in g[v]:
            if visited[i] == visited[v] - 1 and not arr[i]:
                arr[i] = True
                q.append(i)

    return arr

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = bfs(n)

arr = [False for _ in range(n+1)]
arr[1] = True
arr = backtrack(1)

s = set()
dist = [-1 for _ in range(m+1)]
for i in range(2, n):
    if arr[i]:
        if dist[visited[i]] == -1 and visited[i] not in s:
            s.add(visited[i])
            dist[visited[i]] = i
        elif visited[i] in s:
            s.remove(visited[i])

if len(s) > 0:
    print(dist[s.pop()])
else:
    print(1)
