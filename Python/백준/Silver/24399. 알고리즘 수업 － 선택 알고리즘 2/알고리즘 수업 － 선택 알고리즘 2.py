import sys

sys.setrecursionlimit(20 ** 3)

def select(a, p, r, q):
    if p == r:
        return a[p]

    t = partition(a, p, r)
    k = t - p + 1
    if q < k:
        return select(a, p, t-1, q)
    elif q == k:
        return a[t]
    else:
        return select(a, t+1, r, q-k)

def partition(a, p, r):
    global cnt

    x = a[r]
    i = p-1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]

            cnt += 1
            if cnt == v:
                print(*a[1:])
                exit()

    if i + 1 != r:
        a[i+1], a[r] = a[r], a[i+1]

        cnt += 1
        if cnt == v:
            print(*a[1:])
            exit()

    return i+1

n, q, v = map(int, input().split())
a = [0] + list(map(int, input().split()))

cnt = 0
select(a, 1, n, q)
print(-1)
