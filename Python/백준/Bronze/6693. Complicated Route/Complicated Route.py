import re

while True:
    s = input()
    if s == "END":
        break

    s = s[:-1].split(",")
    x, y = 0, 0
    for i in s:
        n = int("".join(re.findall(r'\d+', i)))
        if i.endswith("NE"):
            d = n / (2 ** 0.5)
            x += d
            y += d
        elif i.endswith("SE"):
            d = n / (2 ** 0.5)
            x += d
            y -= d
        elif i.endswith("SW"):
            d = n / (2 ** 0.5)
            x -= d
            y -= d
        elif i.endswith("NW"):
            d = n / (2 ** 0.5)
            x -= d
            y += d
        elif i.endswith("N"):
            y += n
        elif i.endswith("E"):
            x += n
        elif i.endswith("S"):
            y -= n
        elif i.endswith("W"):
            x -= n
    print(f"You can go to ({x:.03f},{y:.03f}), the distance is {(x ** 2 + y ** 2) ** 0.5:.03f} steps.")
