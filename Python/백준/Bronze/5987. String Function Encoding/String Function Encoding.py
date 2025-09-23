for t in range(int(input())):
    n, c, s = input().split()
    for i in range(int(c)):
        s = s[int(n):] + s
    print(s)
