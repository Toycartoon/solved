while True:
    n, *a = map(int, input().split())
    if n == 0:
        break

    v = [0] * a[-1]
    for i in range(n-1, -1, -1):
        for x in range(a[i]):
            v[x] = i+1
    print(*v)
