n = int(input())
g = [[" " for _ in range(n)] for __ in range(n)]
g[0] = ["-"] * n
g[-1] = ["-"] * n

for i in range(n):
    g[i][n-i-1] = "*"
    g[i][i] = "*"

for i in range(n):
    g[i][0] = "|"
    g[i][-1] = "|"

for i in g:
    print(*i, sep="")
