for i in range(int(input())):
    q = 0
    f = True
    n, s = input().split()
    for i in s:
        if i == ">":
            q += 1
        elif i == "<":
            if q == 0:
                f = False
                break
            q -= 1

    if q > 0 or not f:
        print("illegal")
    else:
        print("legal")
