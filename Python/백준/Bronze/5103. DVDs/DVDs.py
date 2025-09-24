while True:
    stock = input()
    if stock == "#":
        break

    m, s = map(int, input().split())
    for t in range(int(input())):
        c, n = input().split()
        if c == "S":
            if s >= int(n):
                s -= int(n)
        elif c == "R":
            s = min(m, s + int(n))
    print(stock, s)
