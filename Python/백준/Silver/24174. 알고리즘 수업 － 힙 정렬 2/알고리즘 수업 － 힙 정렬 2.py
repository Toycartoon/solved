import sys

sys.setrecursionlimit(10 ** 9)

def heap_sort(a, n):
    global cnt, ans

    build_min_heap(a, n)
    for i in range(n, 1, -1):
        a[1], a[i] = a[i], a[1]
        cnt += 1
        if cnt == x:
            print(*a[1:])
            exit()
        heapify(a, 1, i-1)

def build_min_heap(a, n):
    for i in range(n // 2, 0, -1):
        heapify(a, i, n)

def heapify(a, k, n):
    global cnt, ans

    left = 2 * k
    right = 2 * k + 1
    if right <= n:
        if a[left] < a[right]:
            smaller = left
        else:
            smaller = right
    elif left <= n:
        smaller = left
    else:
        return

    if a[smaller] < a[k]:
        a[k], a[smaller] = a[smaller], a[k]
        cnt += 1
        if cnt == x:
            print(*a[1:])
            exit()
        heapify(a, smaller, n)

n, x = map(int, input().split())
a = ["-"] + list(map(int, input().split()))
cnt = 0
heap_sort(a, n)
print(-1)
