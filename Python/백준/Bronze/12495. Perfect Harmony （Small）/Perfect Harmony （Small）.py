for t in range(int(input())):
    n, l, h = map(int, input().split())
    a = list(map(int, input().split()))

    f = "NO"
    for i in range(l, h+1):
        ff = True
        for j in a:
            if max(j, i) % min(i, j) != 0:
                ff = False
                break

        if ff:
            f = i
            break
    print(f"Case #{t+1}: {f}")
