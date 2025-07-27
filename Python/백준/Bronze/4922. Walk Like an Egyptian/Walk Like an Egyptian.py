while True:
    n = int(input())

    if n == 0:
        break

    ans = 1
    v = 0
    for i in range(1, n):
        v += 2
        ans += v

    print(n, "=>", ans)
