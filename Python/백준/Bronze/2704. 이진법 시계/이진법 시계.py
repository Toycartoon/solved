for t in range(int(input())):
    h, m, s = map(int, input().split(":"))
    bh = bin(h)[2:].zfill(6)
    bm = bin(m)[2:].zfill(6)
    bs = bin(s)[2:].zfill(6)

    for i in range(6):
        print(bh[i] + bm[i] + bs[i], end="")
    print(" ", end="")
    print(bh+bm+bs)
