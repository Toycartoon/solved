while True:
    name, r = input().split()
    if name == "#" and r == "0":
        break

    r = int(r)
    while True:
        c, n = input().split()
        if c == "X" and n == "0":
            break

        if c == "B" and r + int(n) <= 68:
            r += int(n)
        elif c == "C" and r - int(n) >= 0:
            r -= int(n)
    print(name, r)
