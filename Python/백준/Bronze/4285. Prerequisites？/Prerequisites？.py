while True:
    r, *c = map(int, input().split())
    if r == 0:
        break

    a = set(map(int, input().split()))
    f = True
    for t in range(c[0]):
        n, m, *k = map(int, input().split())
        if len(set(k) & a) < m:
            f = False

    if f:
        print("yes")
    else:
        print("no")
