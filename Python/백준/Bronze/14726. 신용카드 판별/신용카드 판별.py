for t in range(int(input())):
    s = input()
    a = 0
    for i in range(len(s)):
        if i % 2 == 0:
            a += sum(map(int, [*str(int(s[i]) * 2)]))
        else:
            a += int(s[i])

    if a % 10 == 0:
        print("T")
    else:
        print("F")
