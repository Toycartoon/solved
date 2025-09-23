g = [[*input()] for _ in range(3)]
for i in g:
    if i.count("O") == 3:
        print("O")
        exit()
    elif i.count("X") == 3:
        print("X")
        exit()

for i in zip(*g):
    if i.count("O") == 3:
        print("O")
        exit()
    elif i.count("X") == 3:
        print("X")
        exit()

if g[0][0] == g[1][1] == g[2][2] and g[0][0] != "E":
    print(g[0][0])
    exit()
elif g[0][2] == g[1][1] == g[2][0] and g[0][2] != "E":
    print(g[0][2])
    exit()
print("N")
