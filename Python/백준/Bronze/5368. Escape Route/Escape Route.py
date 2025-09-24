for t in range(int(input())):
    n = int(input())
    g = [[*input()] for _ in range(n)]

    s = (-1, -1)
    p = []
    for y in range(n):
        for x in range(n):
            if g[y][x] == "s":
                s = (y, x)
            elif g[y][x] == "p":
                p.append((y, x))

    d = float('inf')
    idx = ()
    for y, x in p:
        v = ((x - s[1]) ** 2 + (y - s[0]) ** 2) ** 0.5
        if d > v:
            d = v
            idx = (y, x)
    print(f"{"".join(str(s).split())}:{"".join(str(idx).split())}:{d:.02f}")
