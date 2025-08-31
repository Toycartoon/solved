import sys
from collections import deque

input = sys.stdin.readline

q = deque()
def bfs(x):
    q.append(x)
    visited[x] = False
    cnt = []
    while q:
        x = q.popleft()
        if x in w:
            for i in w[x]:
                if not visited[i]:
                    visited[i] = True
                    cnt.append(i)
                    q.append(i)

    return cnt

w = {}
visited = {}
for i in range(int(input())):
    u, v = input().strip().split(" is ")
    if u in w:
        w[u].append(v)
    else:
        w[u] = [v]
    visited[v] = False
    visited[u] = False

ans = bfs("Baba")
for i in sorted(ans):
    print(i)
