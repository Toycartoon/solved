from collections import deque

q = deque()
def bfs(x):
    q.append(x)
    visited[x] = 0
    while q:
        v = q.popleft()
        for i in range(v % g[v], n, g[v]):
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                q.append(i)

n = int(input())
g = list(map(int, input().split()))
visited = [-1 for _ in range(n)]
a, b = map(int, input().split())
bfs(a-1)
print(visited[b-1])
