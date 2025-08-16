while True:
    n = float(input())
    if n == 0:
        break

    t = 0
    i = 2
    while t < n:
        t += 1 / i
        i += 1

    print(f"{i-2} card(s)")
