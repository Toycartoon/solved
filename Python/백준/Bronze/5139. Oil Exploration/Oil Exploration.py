for t in range(int(input())):
    n, m = map(int, input().split())
    g = [[*input()] for _ in range(n)]

    print(f"Data Set {t+1}:")
    a = []
    for i in zip(*g):
        if "X" not in i:
            a.append("N")
            continue
        c = 0
        for v in i:
            if v == "X":
                a.append(c)
                break
            elif v == "H":
                c += 3
            elif v == "S":
                c += 1
    print(*a)
    print()
