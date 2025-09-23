while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break

    x, y = 0, 0
    for i in range(m, n+1):
        j = 0
        for k in range(1, i+1):
            if i % k == 0:
                j += 1

        if j >= y:
            x, y = i, j
    print(x, y)
