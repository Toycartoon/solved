from collections import deque

n, m = map(int, input().split())
p = (list(map(int, input().split())) if n != 0 else [])
visited = [-1 for _ in range(20001)]

q = deque()
def bfs(x):
    q.append(x)
    visited[x] = 0
    while q:
        v = q.popleft()
        for i in p:
            if 0 <= v + i < len(visited):
                if visited[v+i] == -1:
                    visited[v+i] = visited[v] + 1
                    q.append(v+i)

    return visited


ans = bfs(10000)
print(ans[m+10000])
