for t in range(int(input())):
    n, *l = map(int, input().split())
    y = {}
    for i in range(1, 2 * n+1, 2):
        if l[i] in y:
            y[l[i]] += 1
        else:
            y[l[i]] = 1

    print(max(y.values()))
