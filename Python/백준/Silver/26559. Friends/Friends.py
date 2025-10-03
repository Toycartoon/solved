for t in range(int(input())):
    a = []
    for i in range(int(input())):
        s, n = input().split()
        a.append((s, int(n)))
    a.sort(key=lambda x: -x[1])
    v = []
    for i in a:
        v.append(i[0])
    print(*v, sep=", ")
