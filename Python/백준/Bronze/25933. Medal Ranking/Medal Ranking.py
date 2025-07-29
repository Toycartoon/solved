for t in range(int(input())):
    u1, u2, u3, r1, r2, r3 = map(int, input().split())

    cnt, clr = True, True
    if u1 + u2 + u3 <= r1 + r2 + r3:
        cnt = False

    if u1 < r1 or (u1 == r1 and u2 < r2) or (u1 == r1 and u2 == r2 and u3 <= r3):
        clr = False

    print(u1, u2, u3, r1, r2, r3)
    if cnt and clr:
        print("both")
    elif cnt:
        print("count")
    elif clr:
        print("color")
    else:
        print("none")
    print()
