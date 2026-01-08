while True:
    n = int(input())
    if n == 0:
        break

    ans = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            ans += a * b
    print(ans)
