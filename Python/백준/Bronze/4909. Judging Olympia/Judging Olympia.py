while True:
    a = list(map(int, input().split()))
    if a.count(0) == 6:
        break

    print("%g" % (sum(sorted(a)[1:-1]) / 4))
