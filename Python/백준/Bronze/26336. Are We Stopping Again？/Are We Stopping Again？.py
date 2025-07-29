for t in range(int(input())):
    d, o, m = map(int, input().split())
    g = [True for _ in range(d)]

    for i in range(o, len(g), o):
        g[i] = False

    for i in range(m, len(g), m):
        g[i] = False

    print(d, o, m)
    print(g.count(False))
