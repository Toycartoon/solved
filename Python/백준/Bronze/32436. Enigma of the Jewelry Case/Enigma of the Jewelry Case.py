n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

for i in range(4):
    f = True
    for y in range(n):
        if not f:
            break
        for x in range(1, n):
            if g[y][x-1] > g[y][x]:
                f = False
                break

    for y in range(n):
        if not f:
            break
        for x in range(1, n):
            if list(zip(*g))[y][x-1] > list(zip(*g))[y][x]:
                f = False
                break

    if not f:
        g = list(zip(*g[::-1]))
    else:
        print((4-i)%4)
        break
