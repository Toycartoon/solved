while True:
    a = input()
    if a == "0":
        break

    s = set()
    s.add(a)
    while True:
        a = int(a)
        a = ("0" * max(0, 8 - len(str(a ** 2)))) + str(a ** 2)
        a = a[2:-2]
        if a in s:
            break
        s.add(a)
    print(len(s))
