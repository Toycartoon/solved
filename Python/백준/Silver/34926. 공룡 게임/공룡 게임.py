from collections import deque

q = deque()
def bfs(_x):
    visited[_x] = True
    q.append(_x)

    while q:
        x = q.popleft()

        if x+1 < n and s[x+1] == "_" and not visited[x+1]:
            visited[x+1] = True
            q.append(x+1)
        if x+k < n and s[x+k] == "_" and not visited[x+k]:
            visited[x+k] = True
            q.append(x+k)


n, k = map(int, input().split())
s = input()
visited = [False for _ in range(n)]

bfs(0)
if visited[-1]:
    print("YES")
else:
    print("NO")