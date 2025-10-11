for t in range(int(input())):
    g = [0 for _ in range(1001)]
    for i in range(int(input())):
        _, a, b = input().split()
        for v in range(int(a), int(b)):
            g[v] += 1

    for i in g:
        if i != 0:
            print(chr(i+64), end="")
    print()
