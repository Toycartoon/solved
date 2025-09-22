a, b = input().split()
g = [["." for _ in range(len(a))] for __ in range(len(b))]

idx = -1
for i in range(len(a)):
    if a[i] in b:
        idx = a.index(a[i])
        g[b.index(a[i])] = [*a]
        break

for i in range(len(b)):
    g[i][idx] = b[i]

for v in g:
    print(*v, sep="")
