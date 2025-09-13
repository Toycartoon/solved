s = {(0, 0)}
x, y = 0, 0

n = int(input())
l = input()
for i in l:
    if i == "S":
        y -= 1
    elif i == "E":
        x += 1
    elif i == "W":
        x -= 1
    elif i == "N":
        y += 1
    s.add((x, y))

print(len(s))
