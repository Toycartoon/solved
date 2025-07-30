while True:
    a, d, n = map(int, input().split())
    if a == d == n == 0:
        break

    if (n - a) % d != 0 or (n - a) // d < 0:
        print("X")
    else:
        print((n - a) // d + 1)
