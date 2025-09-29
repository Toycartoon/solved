while True:
    n = int(input())
    if n == 0:
        break

    l, r = 0, 1
    s = 1

    ans = 0
    while r < n:
        if s < n:
            r += 1
            s += r
        elif s > n:
            l += 1
            s -= (l-1)
        else:
            ans += 1
            r += 1
            s += r
    print(ans)
