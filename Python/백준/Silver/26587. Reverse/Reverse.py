while True:
    try:
        s = input().split()

        a = []
        v = []
        for i in s:
            if i[0] in "aeiouAEIOU":
                v.append(i)
                a.append(-1)
            else:
                a.append(i)

        v.reverse()
        idx = 0
        for i in a:
            if type(i) == int:
                print(v[idx], end=" ")
                idx += 1
            else:
                print(i, end=" ")
        print()
    except EOFError:
        break