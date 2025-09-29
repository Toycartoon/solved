while True:
    d, n = map(float, input().split())
    if d == n == 0:
        break
    
    a = []
    for i in range(int(n)):
        x, y = map(float, input().split())
        a.append((x, y))

    sour, sweet = 0, 0
    for i in range(int(n)):
        f = True
        for j in range(int(n)):
            if i == j:
                continue
            dist = ((a[i][0]-a[j][0]) ** 2 + (a[i][1]-a[j][1]) ** 2) ** 0.5
            if dist <= d:
                f = False
                break

        if f:
            sweet += 1
        else:
            sour += 1
    print(f"{sour} sour, {sweet} sweet")
