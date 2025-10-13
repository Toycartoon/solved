while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    v = [0 for _ in range(10)]
    for i in a:
        for j in b:
            for k in str(i*j):
                v[int(k)] += 1
    print(*v)
