for t in range(int(input())):
    a = []
    for i in range(int(input())):
        x, y = map(int, input().split())
        a.append((x, y))
    a.sort()

    ans = ()
    d = float('inf')
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            v = ((a[i][0]-a[j][0]) ** 2 + (a[i][1]-a[j][1]) ** 2) ** 0.5
            if d > v:
                d = v
                ans = (a[i], a[j])
    print(*ans[0], *ans[1])
