for t in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    c.reverse()

    ans = 0
    for i in range(n):
        if c[i] % 2 == 1:
            c[i] += 1

    while len({*c}) != 1:
        a = []
        for i in range(n):
            a.append(c[i-1] // 2)

        for i in range(n):
            c[i] = c[i] // 2 + a[i]
            if c[i] % 2 == 1:
                c[i] += 1
        ans += 1
    print(ans)
