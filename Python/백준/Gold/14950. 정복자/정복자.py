import sys
import heapq

input = sys.stdin.readline

def find(i):
    trace = []
    ptr = i
    while arr[ptr] != -1:
        trace.append(ptr)
        ptr = arr[ptr]

    for v in trace:
        arr[v] = ptr

    return ptr

def union(i, j):
    ir = find(i)
    jr = find(j)

    if ir == jr:
        return False

    arr[jr] = ir
    return True

q = []
n, m, t = map(int, input().split())

arr = [-1] * (n + 1)
w = 0

for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

while q:
    k, i, j = heapq.heappop(q)

    f = union(i, j)
    if f:
        w += k

print(w + t * (n-2) * (n-1) // 2)
