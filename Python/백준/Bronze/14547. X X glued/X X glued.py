while True:
    com, *s = input().split()
    if com == "#":
        break

    a = set()
    for i in range(1, 4):
        if s[0][i-1] == s[0][i]:
            a.add(s[0][i])

    a = sorted(list(a))
    if len(a) == 0:
        continue
    elif len(a) == 1:
        print(f"{a[0]} {a[0]} glued")
    else:
        print(f"{a[0]} {a[0]} glued and {a[1]} {a[1]} glued")
