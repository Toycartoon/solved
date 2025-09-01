import heapq
import sys
from math import inf

input = sys.stdin.readline

f, p, c, m = map(int, input().split())
g = [[] for _ in range(f+1)]
dist = [inf for _ in range(f+1)]

q = []
def dijkstra(s):
    dist[s] = 0
    heapq.heappush(q, (0, s))
    while q:
        d, node = heapq.heappop(q)
        if dist[node] < d:
            continue

        for v in g[node]:
            cost = d + v[0]
            if cost < dist[v[1]]:
                dist[v[1]] = cost
                heapq.heappush(q, (cost, v[1]))

for i in range(p):
    u, v, w = map(int, input().split())
    g[u].append((w, v))
    g[v].append((w, u))

dijkstra(1)
ans = []
for i in range(c):
    n = int(input())
    if dist[n] <= m:
        ans.append(i+1)

print(len(ans))
for v in ans:
    print(v)
