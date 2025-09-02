from collections import deque

n = int(input())
g = [[] for _ in range(n)]

q = deque()
def bfs(x, visited):
    q.append(x)
    while q:
        v = q.popleft()
        for i in g[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

    return visited

for i in range(n):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        if a[j] == 1:
            g[i].append(j)

for i in range(n):
    print(*bfs(i, [0 for _ in range(n)]))
