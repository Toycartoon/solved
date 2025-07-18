import sys
import heapq

input = sys.stdin.readline

for t in range(int(input())):
    k = int(input())
    q = list(map(int, input().split()))

    heapq.heapify(q)

    ans = 0
    while len(q) > 1:
        a = heapq.heappop(q)
        b = heapq.heappop(q)

        ans += a + b
        heapq.heappush(q, a + b)

    print(ans)
