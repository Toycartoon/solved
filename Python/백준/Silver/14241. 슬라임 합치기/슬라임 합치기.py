import heapq

n = int(input())
a = list(map(int, input().split()))

heapq.heapify(a)

ans = 0
while len(a) > 1:
    u = heapq.heappop(a)
    v = heapq.heappop(a)
    ans += u * v

    heapq.heappush(a, u+v)

print(ans)
