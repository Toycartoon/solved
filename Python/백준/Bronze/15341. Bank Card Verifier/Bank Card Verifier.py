while True:
    s = input().split()
    if s.count("0000") == 4:
        break

    v = list(map(int, [*("".join(s))]))
    ans = 0
    for i in range(16):
        if i % 2 == 0:
            if v[i] * 2 > 9:
                ans += v[i] * 2 - 9
            else:
                ans += v[i] * 2
        else:
            ans += v[i]

    if ans % 10 == 0:
        print("Yes")
    else:
        print("No")
