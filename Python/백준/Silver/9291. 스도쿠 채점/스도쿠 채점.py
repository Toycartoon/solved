for t in range(int(input())):
    a = [list(map(int, input().split())) for _ in range(9)]

    f = True
    for i in a:
        if len(set(i)) != 9:
            f = False
            break

    for i in zip(*a):
        if len(set(i)) != 9:
            f = False
            break

    for k in range(3):
        for i in range(3, 12, 3):
            s = set()
            for j in range(3):
                s.update(a[3*k+j][i-3:i])
            if len(s) != 9:
                f = False
                break

    if f:
        print(f"Case {t+1}: CORRECT")
    else:
        print(f"Case {t+1}: INCORRECT")

    try:
        input()
    except EOFError:
        break
