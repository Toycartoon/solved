while True:
    n, l, r = map(int, input().split())
    if n == l == r == 0:
        break

    a = []
    for i in range(n):
        a.append(int(input()))

    ans = 0
    for x in range(l, r+1):
        f = True
        for i in range(n):
            if x % a[i] == 0:
                f = False
                if i % 2 == 0:
                    ans += 1
                break

        if f:
            if n % 2 == 0:
                ans += 1
    print(ans)
