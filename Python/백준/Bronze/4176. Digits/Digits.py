while True:
    x = input()
    if x == "END":
        break

    i = 1
    while True:
        b = str(len(x))
        if b == x:
            print(i)
            break
        x = b
        i += 1
