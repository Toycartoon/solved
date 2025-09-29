for z in range(int(input())):
    n = int(input())
    s = input()
    p = input()
    d = ord(s[0])-ord(p)

    for i in s:
        x = ord(i) - d
        if x < 97:
            x += 26
        elif x > 122:
            x -= 26
        print(chr(x), end="")
    print()
