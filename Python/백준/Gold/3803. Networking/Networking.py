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

while True:
    q = []
    p, *r = map(int, input().split())
    if p == 0:
        break

    arr = [-1] * (p + 1)
    w = 0

    for _ in range(r[0]):
        i, j, k = map(int, input().split())
        heapq.heappush(q, (k, i, j))

    while q:
        k, i, j = heapq.heappop(q)

        v = union(i, j)
        if v:
            w += k

    print(w)
    _ = input()
