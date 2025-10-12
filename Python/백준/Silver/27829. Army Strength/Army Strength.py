for t in range(int(input())):
    _ = input()
    ng, nm = map(int, input().split())
    g = list(map(int, input().split()))
    m = list(map(int, input().split()))

    g.sort()
    m.sort()
    idxg, idxm = 0, 0
    while idxg < ng and idxm < nm:
        if g[idxg] < m[idxm]:
            idxg += 1
        else:
            idxm += 1

    if idxg == ng:
        print("MechaGodzilla")
    else:
        print("Godzilla")
