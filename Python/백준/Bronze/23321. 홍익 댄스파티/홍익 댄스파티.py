g = [[*input()] for _ in range(5)]
g = list(zip(*g))

for i in range(len(g)):
    if g[i] == (".", "o", "m", "l", "n"):
        g[i] = ("o", "w", "l", "n", ".")
    elif g[i] == ("o", "w", "l", "n", "."):
        g[i] = (".", "o", "m", "l", "n")

for v in zip(*g):
    print(*v, sep="")
