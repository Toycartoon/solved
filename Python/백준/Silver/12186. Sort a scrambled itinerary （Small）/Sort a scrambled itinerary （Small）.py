for t in range(int(input())):
    n = int(input())

    r = []
    d = {}
    for i in range(n):
        s = input()
        e = input()

        r.append(s)
        d[s] = e

    for i in r:
        x = 0
        v = i
        while v in d:
            v = d[v]
            x += 1

        if x == n:
            tmp = i

    print(f"Case #{t+1}: ", end="")
    while tmp in d:
        nxt = d[tmp]
        print(f"{tmp}-{nxt}", end=" ")
        tmp = nxt
    print()
