while True:
    r, c = map(int, input().split())
    if r == c == 0:
        break

    g = [[*input()] for _ in range(r)]
    ans = [["" for _ in range(c)] for __ in range(r)]
    for y in range(r):
        for x in range(c):
            if g[y][x] == "*":
                ans[y][x] = "*"
                continue

            a = 0
            for n in range(max(y-1, 0), min(y+2, r)):
                for m in range(max(x-1, 0), min(x+2, c)):
                    if g[n][m] == "*":
                        a += 1
            ans[y][x] = a

    for i in ans:
        print(*i, sep="")
