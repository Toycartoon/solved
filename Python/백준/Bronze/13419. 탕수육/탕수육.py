for t in range(int(input())):
    s = input()

    a, b = "", ""
    for i in range(len(s)):
        if i % 2 == 0:
            a += s[i]
        else:
            b += s[i]

    if len(s) % 2 == 1:
        a, b = a + b, b + a

    print(a)
    print(b)
