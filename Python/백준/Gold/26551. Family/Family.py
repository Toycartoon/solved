import sys

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
        return

    arr[jr] = ir

arr = {}
for i in range(int(input())):
    a, _, b = input().strip().split()
    if a not in arr:
        arr[a] = -1
    if b not in arr:
        arr[b] = -1
    union(a, b)

for i in range(int(input())):
    a, b = input().strip().split()
    if find(a) == find(b):
        print("Related")
    else:
        print("Not Related")
