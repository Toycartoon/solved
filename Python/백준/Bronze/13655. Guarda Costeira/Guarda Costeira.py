while True:
    try:
        d, vf, vg = map(int, input().split())
        if 12 / vf >= ((144 + d ** 2) ** 0.5) / vg:
            print("S")
        else:
            print("N")
    except EOFError:
        break
