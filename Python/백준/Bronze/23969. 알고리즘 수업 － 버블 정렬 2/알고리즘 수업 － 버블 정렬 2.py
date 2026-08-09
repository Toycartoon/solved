n, k = map(int, input().split())
a = list(map(int, input().split()))

idx = 0
for last in range(n-1, 0, -1):
    for i in range(last):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            idx += 1
            if idx == k:
                print(*a)
                exit()
print(-1)
