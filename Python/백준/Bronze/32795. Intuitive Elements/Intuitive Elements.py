for t in range(int(input())):
    a = input()
    b = input()

    f = True
    for i in b:
        if i not in a:
            f = False
            break

    if f:
        print("YES")
    else:
        print("NO")
