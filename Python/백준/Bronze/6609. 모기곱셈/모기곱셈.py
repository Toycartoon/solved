while True:
    try:
        m, p, l, e, r, s, n = map(int, input().split())
        for i in range(n):
            tmp = m
            m = p // s
            p = l // r
            l = tmp * e
        print(m)
    except EOFError:
        break
