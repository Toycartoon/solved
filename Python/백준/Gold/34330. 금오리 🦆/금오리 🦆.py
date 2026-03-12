import sys

input = sys.stdin.readline

def find(ptr):
    trace = []
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


r, l = map(int, input().split())
n, m = map(int, input().split())

leaf = []
arr = [-1 for _ in range(n+1)]
for i in range(n):
    x, y, ri = map(int, input().split())
    leaf.append((x, y, ri))

    d = x ** 2 + y ** 2
    if max(0, r-ri) ** 2 <= d:
        union(0, i+1)

    for j in range(len(leaf)-1):
        xj, yj, rj = leaf[j]
        d = (x - xj) ** 2 + (y - yj) ** 2
        if d <= (ri + rj) ** 2:
            union(i+1, j+1)

quack = 0   # 꽥
for i in range(m):
    x, y = map(int, input().split())
    d = (x ** 2) + (y ** 2)
    if max(0, r-l) ** 2 <= d:
        quack += 1
        continue

    for j in range(1, n+1):
        if find(0) != find(j):
            continue

        xi, yi, ri = leaf[j-1]
        d = (x - xi) ** 2 + (y - yi) ** 2
        if d <= (l+ri) ** 2:
            quack += 1
            break
print(quack)
