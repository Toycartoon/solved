while True:
    s = input().split()
    if s == ["#"]:
        break

    c, t = 0, 0
    for i in s:
        if i == "*":
            break
        if i == "A" or int(i) % 2 == 1:
            c += 1
        else:
            t += 1

    if c > t:
        print("Cheryl")
    elif c < t:
        print("Tania")
    else:
        print("Draw")
