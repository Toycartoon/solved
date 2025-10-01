while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == s1 == r0 == r1 == 0:
        break

    if f"{s0}{s1}" == "12" or f"{s0}{s1}" == "21":
        if f"{r0}{r1}" == "12" or f"{r0}{r1}" == "21":
            print("Tie.")
        else:
            print("Player 1 wins.")
    elif f"{r0}{r1}" == "12" or f"{r0}{r1}" == "21":
        if f"{s0}{s1}" == "12" or f"{s0}{s1}" == "21":
            print("Tie.")
        else:
            print("Player 2 wins.")
    elif s0 == s1:
        if r0 == r1:
            if s0 == r0:
                print("Tie.")
            elif s0 > r0:
                print("Player 1 wins.")
            else:
                print("Player 2 wins.")
        else:
            print("Player 1 wins.")
    elif r0 == r1:
        if s0 == s1:
            if s0 == r0:
                print("Tie.")
            elif s0 > r0:
                print("Player 1 wins.")
            else:
                print("Player 2 wins.")
        else:
            print("Player 2 wins.")
    else:
        s = str(max(s1, s0)) + str(min(s0, s1))
        r = str(max(r1, r0)) + str(min(r0, r1))
        if s > r:
            print("Player 1 wins.")
        elif r > s:
            print("Player 2 wins.")
        else:
            print("Tie.")
