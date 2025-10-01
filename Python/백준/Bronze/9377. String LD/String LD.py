while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        a.append(input())

    idx = 0
    while True:
        s = set()
        f = True
        for i in a:
            if len(i[idx+1:]) == 0 or i[idx+1:] in s:
                f = False
                break
            s.add(i[idx+1:])

        if f:
            idx += 1
        else:
            break
    print(idx)
