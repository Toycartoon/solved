for t in range(int(input())):
    n = int(input())
    f = False
    for b in range(2, 65):
        a = ""
        x = n
        while x >= b:
            m = x % b
            x //= b

            if m < 10:
                a += str(m)
            else:
                a += chr(m + 55)

        m = x % b
        if m < 10:
            a += str(m)
        else:
            a += chr(m + 55)

        if a[::-1] == a:
            f = True
            break
    print(int(f))
