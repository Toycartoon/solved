for t in range(int(input())):
    n, v = map(int, input().split())
    a = []
    for i in range(n):
        d, p = map(int, input().split())
        a.append((d, p))

    ans = 0
    for i in range(v):
        a1, a2, c = map(int, input().split())
        if a[a1-1][0] == 1:
            ans += a[a1-1][1]
        if a[a2-1][0] == 1:
            ans += a[a2-1][1]

        if c == 1 and a[a1-1][0] == 0:
            ans += a[a1-1][1]
        if c == 2 and a[a2-1][0] == 0:
            ans += a[a2-1][1]
    print(f"Data Set {t+1}:")
    print(ans)
    print()
