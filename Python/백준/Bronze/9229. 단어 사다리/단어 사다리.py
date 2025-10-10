while True:
    s = input()
    if s == "#":
        break

    f = True
    while True:
        v = input()
        if v == "#":
            break
        elif not f:
            continue

        if len(s) != len(v):
            f = False

        a = 0
        for i in range(len(s)):
            if s[i] != v[i]:
                a += 1

        if a != 1:
            f = False
        s = v

    if f:
        print("Correct")
    else:
        print("Incorrect")
