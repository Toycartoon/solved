w = {"*": 0}
a = input()
b = input()

f = True
for i in b:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

for i in a:
    try:
        if w[i] > 0:
            w[i] -= 1
        else:
            if w["*"] > 0:
                w["*"] -= 1
            else:
                f = False
                break
    except KeyError:
        if w["*"] > 0:
            w["*"] -= 1
        else:
            f = False
            break

print("A" if f else "N")
