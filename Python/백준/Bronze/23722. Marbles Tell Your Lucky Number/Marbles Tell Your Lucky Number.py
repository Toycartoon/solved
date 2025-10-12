while True:
    a = list(map(int, input().split()))
    if a.count(0) == 4:
        break

    while len(a) > 1:
        a.sort()
        for i in range(1, len(a)):
            a[i] -= a[0]
        na = []
        for i in a:
            if i != 0:
                na.append(i)
        a = na
    print(a[0])
