import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
a = []
for i in range(k):
    v, c = map(int, input().split())
    a.append((v, c))

a.sort(key=lambda x: (x[1], -x[0]))
ans = []
s = 0
for i in range(n):
    heapq.heappush(ans, a[i])
    s += a[i][0]

i = n
while s < m and i < k:
    x = heapq.heappop(ans)
    s -= x[0]

    heapq.heappush(ans, a[i])
    s += a[i][0]
    i += 1

if s >= m:
    print(max(ans, key=lambda x: x[1])[1])
else:
    print(-1)
