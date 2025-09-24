for k in range(int(input())):
    a = []
    for t in range(int(input())):
        r, g, b = map(int, input().split())
        a.append((r, g, b))

    d = 0
    idx = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            x = ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2 + (a[i][2] - a[j][2]) ** 2) ** 0.5
            if x > d:
                d = x
                idx = [(i+1, j+1)]
            elif x == d:
                idx.append((i+1, j+1))

    print(f"Data Set {k+1}:")
    for i in idx:
        print(*i)
