while True:
    try:
        n = int(input())
        a = list(map(int, input().split()))

        if n == 1:
            print(1)
            continue

        d = a[-1] - a[-2]
        f = True
        for i in range(n-1, 0, -1):
            if a[i-1] + d != a[i]:
                print(i+1)
                f = False
                break

        if f:
            print(1)
    except EOFError:
        break
