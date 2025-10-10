while True:
    s = list(map(int, [*input()]))
    if s[0] == 0:
        break

    if s[s.index(max(s))] % 2 == 0:
        s[s.index(max(s))] = (s[s.index(max(s))] + 4) % 10
    else:
        s[s.index(max(s))] = 0
    print(int("".join(list(map(str, s)))))
