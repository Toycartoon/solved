while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    a = list(map(int, input().split()))
    t = [0 for _ in range(n+1)]
    for i in a:
        t[i] += 1

    ans = 0
    for i in t:
        if i > 1:
            ans += 1
    print(ans)
