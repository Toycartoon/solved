for t in range(int(input())):
    n = int(input())

    r = []
    d = {}
    for i in range(n-1):
        s, e = input().split()
        r.append(s)
        d[s] = e

    for i in r:
        x = 0
        v = i
        while v in d:
            v = d[v]
            x += 1

        if x == n-1:
            tmp = i

    print(f"Scenario #{t+1}:")
    print(tmp)
    while tmp in d:
        tmp = d[tmp]
        print(tmp)
    print()
