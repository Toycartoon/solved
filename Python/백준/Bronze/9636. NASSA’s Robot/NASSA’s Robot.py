for t in range(int(input())):
    s = input()
    mnx, mny, mxx, mxy = 0, 0, 0, 0
    for i in s:
        if i == "?":
            mnx -= 1
            mny -= 1
            mxx += 1
            mxy += 1
        elif i == "U":
            mny += 1
            mxy += 1
        elif i == "R":
            mnx += 1
            mxx += 1
        elif i == "L":
            mnx -= 1
            mxx -= 1
        elif i == "D":
            mny -= 1
            mxy -= 1
    print(mnx, mny, mxx, mxy)
