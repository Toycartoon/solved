pt, p1, p2 = input().split()
pt = int("".join(pt.split(".")))
p1 = int("".join(p1.split(".")))
p2 = int("".join(p2.split(".")))

f = False
for i in range((pt + p1 - 1) // p1 + 1):
    for j in range((pt + p2 - 1) // p2 + 1):
        if p1 * i + p2 * j == pt:
            print(i, j)
            f = True

if not f:
    print("none")
