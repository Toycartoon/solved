n, m = map(int, input().split())
g = [input() for _ in range(n)]

for y in range(n):
    f = True
    for x in g[y].split("."):
        if x == "":
            continue
        print(len(x), end=" ")
        f = False
    if f:
        print(0)
    else:
        print()

for x in zip(*g):
    f = True
    for y in "".join(x).split("."):
        if y == "":
            continue
        print(len(y), end=" ")
        f = False
    if f:
        print(0)
    else:
        print()
