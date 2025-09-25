s = input()
for i in range(7):
    a = input()
    if s == a:
        print("WINNER")
        break
    elif i == 6:
        print("LOSER")
        break

    for v in range(5):
        if a[v] in s:
            if a[v] == s[v]:
                print("G", end="")
            else:
                print("Y", end="")
        else:
            print("X", end="")
    print()
