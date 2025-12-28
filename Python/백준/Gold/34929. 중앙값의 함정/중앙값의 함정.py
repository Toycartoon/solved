import heapq

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(a[0])
    exit()

heapq.heapify(a)
print(sorted(a)[-2])
while len(a) >= 3:
    u = heapq.heappop(a)
    v = heapq.heappop(a)
    w = heapq.heappop(a)
    
    print(u, v, w)
    heapq.heappush(a, v)
