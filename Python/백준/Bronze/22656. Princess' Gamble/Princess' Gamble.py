while True:
    n, m, p = map(int, input().split())
    if n == m == p == 0:
        break

    x = []
    for i in range(n):
        x.append(int(input()))

    if x[m-1] == 0:
        print(0)
    else:
        print((sum(x) * 100 - sum(x) * p) // x[m-1])
