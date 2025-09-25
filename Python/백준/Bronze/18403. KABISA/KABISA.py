for t in range(int(input())):
    a = eval(f"[{input()}]")
    for i in a:
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i, end=" ")
    print()
