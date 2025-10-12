for t in range(int(input())):
    m, n = input().split()
    if m == "1":
        v = ""
        for i in n.split("."):
            v += bin(int(i))[2:].zfill(8)
        print(int(v, 2))
    elif m == "2":
        n = bin(int(n))[2:].zfill(64)
        v = []
        for i in range(8, 65, 8):
            v.append(int(n[i-8:i], 2))
        print(*v, sep=".")
