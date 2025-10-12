while True:
    n = input()
    if n == "0":
        break

    s = sum(map(int, [*n]))
    p = 11
    while True:
        v = str(int(n) * p)
        if sum(map(int, [*v])) == s:
            print(p)
            break
        p += 1
