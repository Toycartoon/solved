n, k = map(int, input().split())
a = list(map(int, input().split()))

idx = 0
for i in range(1, n):
    loc = i-1
    newItem = a[i]

    while 0 <= loc and newItem < a[loc]:
        a[loc+1] = a[loc]
        idx += 1
        if idx == k:
            print(*a)
            exit()
        loc -= 1

    if loc + 1 != i:
        a[loc+1] = newItem
        idx += 1
        if idx == k:
            print(*a)
            exit()
print(-1)
