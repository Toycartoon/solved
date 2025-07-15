for t in range(int(input())):
    n, m = map(int, input().split())
    g = [0 for _ in range(n)]

    for i in range(m):
        v = list(map(int, input().split()))
        for x in range(n):
            g[x] += v[x]

    print(g.index(max(g)) + 1)
