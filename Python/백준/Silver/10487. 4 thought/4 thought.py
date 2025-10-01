from itertools import product as prod

for t in range(int(input())):
    n = int(input())

    f = ""
    for oper in prod(["+", "-", "*", "//"], repeat=3):
        if eval(f"4{oper[0]}4{oper[1]}4{oper[2]}4=={n}"):
            f = f"4 {oper[0]} 4 {oper[1]} 4 {oper[2]} 4 = {n}".replace("//", "/")

    if f == "":
        print("no solution")
    else:
        print(f)
