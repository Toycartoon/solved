import sys

sys.setrecursionlimit(20 ** 4)

def partition(p, r):
    global ex, ans

    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
            ex += 1
            if ex == k:
                ans = tuple(a)

    if i + 1 != r:
        a[i+1], a[r] = a[r], a[i+1]
        ex += 1
        if ex == k:
            ans = tuple(a)

    return i + 1


def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)
        quick_sort(q+1, r)


n, k = map(int, input().split())
a = list(map(int, input().split()))

ex = 0
ans = ()
quick_sort(0, n-1)

if len(ans) == 0:
    print(-1)
else:
    print(*ans)
