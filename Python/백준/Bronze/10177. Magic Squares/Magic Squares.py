for t in range(int(input())):
    n = int(input())

    g = [list(map(int, input().split())) for _ in range(n)]
    s = sum(g[0])

    f = True
    for i in range(n):
        if sum(g[i]) != s:
            f = False
            break

    for i in range(n):
        if sum(list(zip(*g))[i]) != s:
            f = False
            break

    v = 0
    for i in range(n):
        v += g[i][i]

    if v != s:
        f = False

    v = 0
    for i in range(n):
        v += g[i][n-i-1]

    if v != s:
        f = False

    if f:
        print(f"Magic square of size {n}")
    else:
        print(f"Not a magic square")
