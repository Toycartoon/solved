for t in range(int(input())):
    n = int(input())

    mx = 0
    while 3 ** mx <= n:
        mx += 1

    ans = []
    for i in range(mx-1, -1, -1):
        if 3 ** i <= n:
            ans.append(n // (3 ** i))
            n -= (3 ** i) * (n // 3 ** i)
        else:
            ans.append(0)
    print(*ans)
