for t in range(int(input())):
    _ = input()
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    c = sum(a) / n
    d = sum(b)
    ans = 0
    for i in range(n):
        if a[i] < c:
            if (d + a[i]) / (m + 1) > d / m:
                ans += 1

    print(ans)
