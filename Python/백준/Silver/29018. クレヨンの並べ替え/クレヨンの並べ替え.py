while True:
    s = input()
    if s == "#":
        break

    l = []
    u = []
    n = []
    for i in s:
        if i.islower():
            l.append(i)
        elif i.isupper():
            u.append(i)
        elif i.isnumeric():
            n.append(i)

    l.sort()
    u.sort()
    n.sort()
    print("".join(l)+"".join(u)+"".join(n))
