r, c = map(int, input().split())
g = []
for i in range(r):
    s = input()
    g.append([*(s + s[::-1])])
a, b = map(int, input().split())

for i in range(r-1, -1, -1):
    g.append(g[i][:])

if g[a-1][b-1] == ".":
    g[a-1][b-1] = "#"
else:
    g[a-1][b-1] = "."

for i in g:
    print(*i, sep="")
