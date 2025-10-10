while True:
    m, nmin, nmax = map(int, input().split())
    if m == nmin == nmax == 0:
        break

    p = []
    for i in range(m):
        p.append(int(input()))

    d = []
    for i in range(nmin, nmax+1):
        d.append(p[i-1]-p[i])
    print(nmax-d[::-1].index(max(d)))
