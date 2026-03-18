from math import ceil
from collections import deque

visited = {}

q = deque()
def bfs(x):
    visited[x] = 0
    q.append(x)
    while q:
        v = q.popleft()

        if visited[v] + ceil(n / 3) <= m:
            s = ""
            for i in range(n):
                if not i % 3:
                    s += str(int(not int(v[i])))
                else:
                    s += v[i]

            if s not in visited:
                visited[s] = visited[v] + ceil(n / 3)
                q.append(s)
        if visited[v] + ceil(n / 2) <= m:
            s = ""
            for i in range(n):
                if not i % 2:
                    s += str(int(not int(v[i])))
                else:
                    s += v[i]

            if s not in visited:
                visited[s] = visited[v] + ceil(n / 2)
                q.append(s)
        if visited[v] + n // 2 <= m:
            s = ""
            for i in range(n):
                if i % 2:
                    s += str(int(not int(v[i])))
                else:
                    s += v[i]

            if s not in visited:
                visited[s] = visited[v] + n // 2
                q.append(s)
        if visited[v] + n <= m:
            s = ""
            for i in range(n):
                s += str(int(not int(v[i])))

            if s not in visited:
                visited[s] = visited[v] + n
                q.append(s)


n, m = map(int, input().split())
bfs('0' * n)

print(len(visited))
