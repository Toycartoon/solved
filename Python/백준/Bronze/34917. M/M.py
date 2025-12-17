for t in range(int(input())):
    n = int(input())
    g = [["." for _ in range(n)] for __ in range(n)]
    for i in range(n):
        g[i][0] = "#"
        g[i][-1] = "#"

    for i in range((n+1) // 2):
        g[i][i] = "#"
        g[i][-i-1] = "#"

    for i in g:
        print(*i, sep="")
