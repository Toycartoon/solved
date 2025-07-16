while True:
    g, *ymd = input().split()

    if g == "#":
        break

    y, m, d = map(int, ymd)
    if y > 31 or (y == 31 and m > 4):
        print("?", y-30, m, d)
    else:
        print(g, y, m, d)
