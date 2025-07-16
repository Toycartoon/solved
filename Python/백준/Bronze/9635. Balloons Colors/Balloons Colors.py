for t in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    if a[0] == x and a[-1] == y:
        print("BOTH")
    elif a[0] == x:
        print("EASY")
    elif a[-1] == y:
        print("HARD")
    else:
        print("OKAY")
