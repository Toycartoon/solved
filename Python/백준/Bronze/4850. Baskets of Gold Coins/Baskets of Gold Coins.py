while True:
    try:
        n, w, d, coin = map(int, input().split())
        ans = ((n - 1) * n // 2 * w - coin) // d
        if ans == 0:
            print(n)
        else:
            print(ans)
    except EOFError:
        break