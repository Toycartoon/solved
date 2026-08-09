m, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

l, r = 0, a[-1] + 1
while l + 1 < r:
    mid = (l + r) // 2

    k = 0
    for i in a:
        k += i // mid

    if k >= m:
        l = mid
    elif k < m:
        r = mid

print(l)
