for t in range(int(input())):
    n = int(input())

    f = 1
    g = 1
    for i in range(n):
        if i % 2 == 0:
            f += g
        else:
            g += f

    print(f"Scenario {t+1}:")
    if n % 2 == 1:
        print(f)
    else:
        print(g)
    print()
