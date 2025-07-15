for t in range(int(input())):
    x, k, h = map(int, input().split())
    ans = 0

    k -= h
    ans += 2 * h * x

    m = 0
    if k > 140:
        m = k - 140

    ans += 1.5 * m * x
    ans += (k - m) * x
    print(format(int(ans), ","))
