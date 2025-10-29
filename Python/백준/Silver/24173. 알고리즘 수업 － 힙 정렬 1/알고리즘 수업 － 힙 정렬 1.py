import sys

sys.setrecursionlimit(10 ** 9)

def heap_sort(a, n):
    global cnt, ans

    build_min_heap(a, n)
    for i in range(n, 1, -1):
        a[1], a[i] = a[i], a[1]
        cnt += 1
        if cnt == x:
            ans = (a[i], a[1])
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
            ans = (a[k], a[smaller])
        heapify(a, smaller, n)

n, x = map(int, input().split())
a = ["-"] + list(map(int, input().split()))
cnt = 0
ans = -1
heap_sort(a, n)
if type(ans) == int:
    print(ans)
else:
    print(*ans)
