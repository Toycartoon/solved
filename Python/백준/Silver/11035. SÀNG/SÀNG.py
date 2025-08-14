while True:
    try:
        n, k = map(int, input().split())
        g = [i for i in range(n+1)]
        g[1] = 0

        f = 0
        ans = 0
        for i in range(2, len(g)):
            if g[i] == 0:
                continue
            for j in range(i, len(g), i):
                if g[j] != 0:
                    f += 1
                if f == k:
                    ans = j
                    break
                g[j] = 0
        print(ans)
    except EOFError:
        break
