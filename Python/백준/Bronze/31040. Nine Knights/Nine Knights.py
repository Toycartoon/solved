n = int(input())
for t in range(n):
    g = [[*input()] for _ in range(5)]
    pos = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (2, -1), (1, -2)]

    f = True
    for y in range(5):
        for x in range(5):
            if g[y][x] != "k":
                continue

            for dx, dy in pos:
                if 0 <= x+dx < 5 and 0 <= y+dy < 5:
                    if g[y+dy][x+dx] == "k":
                        f = False
                        break
    if f:
        print("valid")
    else:
        print("invalid")

    if t < n-1:
        input()
