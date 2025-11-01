while True:
    try:
        a = []
        while True:
            s = input()
            if s == "START":
                continue
            elif s == "END":
                break

            name, day, weight = s.split()
            a.append((name, int(day), int(weight)))
        a.sort(key=lambda x: (x[2]-x[1]), reverse=True)
        for i in a:
            print(i[0])
        print()
    except EOFError:
        break
