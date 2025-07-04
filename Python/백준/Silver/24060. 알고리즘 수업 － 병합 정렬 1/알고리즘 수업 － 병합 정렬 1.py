from math import floor
import sys

sys.setrecursionlimit(10 ** 6)

def merge_sort(a, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    i, j = p, q+1
    tmp = []
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    while i <= q:
        tmp.append(a[i])
        i += 1

    while j <= r:
        tmp.append(a[j])
        j += 1

    i, t = p, 0
    while i <= r:
        a[i] = tmp[t]
        ans.append(tmp[t])
        i += 1
        t += 1


n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
merge_sort(a, 0, n-1)
print(ans[k-1] if len(ans) >= k else -1)
