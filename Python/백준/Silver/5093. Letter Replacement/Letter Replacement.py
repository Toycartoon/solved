while True:
    s = input()
    if s == "#":
        break

    a = set()
    w = []
    for i in s:
        if i.lower() in a and i.lower() not in w:
            w.append(i.lower())

        if i.lower() in w:
            print("*?/+!"[w.index(i.lower())], end="")
        else:
            print(i, end="")
        a.add(i.lower())
    print()
