while True:
    a, c, b = input().split()

    if a == b == "0" and c == "W":
        break

    if c == "W":
        if int(a) - int(b) < -200:
            print("Not allowed")
        else:
            print(int(a) - int(b))
    elif c == "D":
        print(int(a) + int(b))
