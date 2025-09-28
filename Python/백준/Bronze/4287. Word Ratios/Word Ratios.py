while True:
    s = input().split()
    if s == ["#"]:
        break

    a, b = s[0], s[1]
    v = ""
    for i in range(len(a)):
        d = ord(b[i])-ord(a[i])
        if d < 0:
            d += 26

        if ord(s[2][i]) + d > 122:
            v += chr(ord(s[2][i]) + d - 26)
        else:
            v += chr(ord(s[2][i]) + d)
    print(*(s + [v]))
