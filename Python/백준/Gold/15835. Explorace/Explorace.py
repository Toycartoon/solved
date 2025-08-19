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

for t in range(int(input())):
    q = []
    n, m = map(int, input().split())

    arr = [-1] * (n + 1)
    w = 0

    for _ in range(m):
        i, j, k = map(int, input().split())
        heapq.heappush(q, (k, i, j))

    while q:
        k, i, j = heapq.heappop(q)

        v = union(i, j)
        if v:
            w += k

    print(f"Case #{t+1}: {w} meters")
