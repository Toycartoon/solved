t = 1
while True:
    p, s = map(int, input().split())
    if p == 0:
        break

    print(f"Hole #{t}")
    if s == 1:
        print("Hole-in-one.")
    else:
        v = s - p
        if v == -3:
            print("Double Eagle.")
        elif v == -2:
            print("Eagle.")
        elif v == -1:
            print("Birdie.")
        elif v == 0:
            print("Par.")
        elif v == 1:
            print("Bogey.")
        else:
            print("Double Bogey.")
    print()
    t += 1
