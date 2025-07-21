c = [True, False, False]
s = input()

for i in s:
    match i:
        case "A":
            c[0], c[1] = c[1], c[0]
        case "B":
            c[1], c[2] = c[2], c[1]
        case "C":
            c[0], c[2] = c[2], c[0]

print(c.index(True) + 1)
