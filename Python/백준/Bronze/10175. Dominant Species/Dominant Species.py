for t in range(int(input())):
    a = [0, 0, 0, 0]
    name, s = input().split()
    for i in s:
        if i == "B":
            a[0] += 2
        elif i == "C":
            a[1] += 1
        elif i == "M":
            a[2] += 4
        elif i == "W":
            a[3] += 3

    if a.count(max(a)) > 1:
        print(f"{name}: There is no dominant species")
    else:
        v = ""
        if a.index(max(a)) == 0:
            v = "Bobcat"
        elif a.index(max(a)) == 1:
            v = "Coyote"
        elif a.index(max(a)) == 2:
            v = "Mountain Lion"
        else:
            v = "Wolf"
        print(f"{name}: The {v} is the dominant species")
