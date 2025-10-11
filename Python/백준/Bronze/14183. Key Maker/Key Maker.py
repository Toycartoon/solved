while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    a = list(map(int, input().split()))

    ans = 0
    for _ in range(n):
        v = list(map(int, input().split()))
        f = True
        for i in range(m):
            if v[i] > a[i]:
                f = False
                break

        if f:
            ans += 1
    print(ans)
