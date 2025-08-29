for q in range(int(input())):
    a, b = map(int, input().split())

    i = b - a if b - a >= 0 else b - a + 43
    o = a - b if a - b >= 0 else a - b + 43

    if i < o:
        print("Inner circle line")
    elif o < i:
        print("Outer circle line")
    else:
        print("Same")
