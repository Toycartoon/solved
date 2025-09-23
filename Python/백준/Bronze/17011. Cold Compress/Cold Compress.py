for t in range(int(input())):
    s = input()
    a = []
    v = 1
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            v += 1
        else:
            a.append(v)
            a.append(s[i-1])
            v = 1
    a.append(v)
    a.append(s[-1])
    print(*a)
