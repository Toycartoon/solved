def check(g):
    for i in range(3):
        if g[i].count("X") == 3 or g[i].count("O") == 3:
            return True

    for i in range(3):
        if list(zip(*g))[i].count("X") == 3 or list(zip(*g))[i].count("O") == 3:
            return True

    if g[0][0] == g[1][1] == g[2][2] and (g[0][0] == "X" or g[0][0] == "O"):
        return True

    if g[2][0] == g[1][1] == g[0][2] and (g[1][1] == "X" or g[1][1] == "O"):
        return True
    return False

ox = input()
g = [[*input()] for __ in range(3)]
for y in range(3):
    for x in range(3):
        if g[y][x] == "E":
            g[y][x] = ox
            if check(g):
                print(y+1, x+1)
                exit()
            g[y][x] = "E"
