while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    d = n - m
    a = d // 2
    b = d % 2

    if b == 1:
        if a > 0:
            a -= 1
        else:
            b = 0

    print(a, b)
