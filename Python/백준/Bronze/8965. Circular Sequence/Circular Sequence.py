for t in range(int(input())):
    s = input()
    a = [s]
    for i in range(len(s)):
        s = s[1:] + s[0]
        a.append(s)

    a.sort()
    print(a[0])
