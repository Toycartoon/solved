while True:
    try:
        n, m = map(int, input().split())
        ans = 0
        for i in range(n, m+1):
            if len({*str(i)}) == len(str(i)):
                ans += 1
        print(ans)
    except EOFError:
        break
