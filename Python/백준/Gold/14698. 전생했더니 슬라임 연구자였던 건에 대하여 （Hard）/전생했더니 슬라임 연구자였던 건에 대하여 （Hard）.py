import heapq
import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input())
    q = list(map(int, input().split()))
    heapq.heapify(q)

    ans = 1
    while len(q) > 1:
        v = heapq.heappop(q)
        u = heapq.heappop(q)
        ans = ans * u * v % 1000000007
        heapq.heappush(q, u * v)
    print(ans)
