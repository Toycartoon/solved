while True:
    a = input()
    b = input()
    if a == b == "E":
        break

    p1, p2 = 0, 0
    for i in range(len(a)):
        if (a[i] == "R" and b[i] == "S") or (a[i] == "S" and b[i] == "P") or (a[i] == "P" and b[i] == "R"):
            p1 += 1
        elif (b[i] == "R" and a[i] == "S") or (b[i] == "S" and a[i] == "P") or (b[i] == "P" and a[i] == "R"):
            p2 += 1

    print(f"P1: {p1}")
    print(f"P2: {p2}")
