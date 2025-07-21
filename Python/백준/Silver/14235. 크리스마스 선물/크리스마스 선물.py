import heapq

q = []
for i in range(int(input())):
    a, *s = map(int, input().split())

    if a == 0:
        print(-heapq.heappop(q) if len(q) > 0 else -1)
    else:
        for v in s:
            heapq.heappush(q, -v)
