t, n = map(int, input().split())
for i in range(t):
    s = input()
    f = True
    h = s.count(s[0]) > 1
    for v in s:
        if (h and s.count(v) == 1) or (not h and s.count(v) > 1):
            f = False
            break
        h = not h

    if f:
        print("T")
    else:
        print("F")
