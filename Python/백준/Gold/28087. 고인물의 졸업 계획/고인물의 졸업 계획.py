import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
x = []
v = 0
for i in range(m):
    s = int(input())
    if s > 2 * n:
        continue
    v += s
    heapq.heappush(x, (s, i+1))
    while v > 2 * n:
        a, _ = heapq.heappop(x)
        v -= a

    if n <= v <= 2 * n:
        print(len(x))
        for t in x:
            print(t[1])
        break
