for t in range(int(input())):
    x, y = 0, 0
    dx, dy = -1, -1

    ans = (0, 0, 0)
    while dx != 0 or dy != 0:
        dx, dy = map(int, input().split())
        x += dx
        y += dy
        d = (x ** 2 + y ** 2) ** 0.5
        if d > ans[0] or (d == ans[0] and x > ans[1]):
            ans = (d, x, y)
    print(ans[1], ans[2])
