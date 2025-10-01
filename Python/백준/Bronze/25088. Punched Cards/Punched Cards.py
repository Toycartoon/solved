for t in range(int(input())):
    r, c = map(int, input().split())
    g = []
    for i in range(2 * r + 1):
        if i % 2 == 0:
            g.append(["+"] + ["-", "+"] * c)
        else:
            g.append(["|"] + [".", "|"] * c)

    for y in range(2):
        for x in range(2):
            g[y][x] = "."

    print(f"Case #{t+1}:")
    for v in g:
        print(*v, sep="")
