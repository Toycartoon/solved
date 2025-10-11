for t in range(int(input())):
    v = 0
    for i in range(int(input())):
        s, r = map(int, input().split())
        v += s * r
    print(1296 // v, 2592 // v, 3888 // v)
