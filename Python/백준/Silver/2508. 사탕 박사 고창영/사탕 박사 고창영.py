for t in range(int(input())):
    _ = input()
    r, c = map(int, input().split())
    g = [[*input()] for _ in range(r)]

    ans = 0
    for y in range(r):
        for x in range(c):
            if g[y][x] == "o":
                if 0 < y < r-1 and g[y-1][x] == "v" and g[y+1][x] == "^":
                    ans += 1
                if 0 < x < c-1 and g[y][x-1] == ">" and g[y][x+1] == "<":
                    ans += 1

    print(ans)
