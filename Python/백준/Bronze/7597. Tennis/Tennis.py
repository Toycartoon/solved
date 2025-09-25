while True:
    s = input()
    if s == "#":
        break

    a, b = 0, 0
    ga, gb = 0, 0
    for i in s:
        if i == "A":
            a += 1
        elif i == "B":
            b += 1

        if abs(a - b) >= 2 and max(a, b) >= 4:
            if a > b:
                ga += 1
            elif b > a:
                gb += 1
            a, b = 0, 0
    print(f"A {ga} B {gb}")
