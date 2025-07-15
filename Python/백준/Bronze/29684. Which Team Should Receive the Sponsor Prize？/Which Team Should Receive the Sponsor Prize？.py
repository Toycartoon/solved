while True:
    n = int(input())

    if n == 0:
        break

    a = list(map(int, input().split()))
    g = []
    for i in a:
        g.append(abs(i-2023))

    print(g.index(min(g))+1)
