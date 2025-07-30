for t in range(int(input())):
    w = {}
    a = input().split()

    for i in a:
        if i[0] in w:
            w[i[0]] += 1
        else:
            w[i[0]] = 1

    print(max(w.values()))
