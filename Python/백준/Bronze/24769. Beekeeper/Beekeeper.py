while True:
    n = int(input())
    if n == 0:
        break
    a = []
    for i in range(n):
        s = input()
        v = 0
        for x in ("aa", "ee", "ii", "oo", "uu", "yy"):
            v += s.count(x)
        a.append((s, v))
    a.sort(key=lambda x: -x[1])
    print(a[0][0])
