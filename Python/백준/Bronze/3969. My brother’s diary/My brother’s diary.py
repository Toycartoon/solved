for t in range(int(input())):
    a = [0 for _ in range(26)]
    s = input()
    for i in s:
        if i.isalpha():
            a[ord(i)-65] += 1

    if a.count(max(a)) > 1:
        print("NOT POSSIBLE")
        continue

    d = 4-a.index(max(a))
    if d > 0:
        d -= 26
    print(-d, end=" ")
    for i in s:
        if i.isalpha():
            v = ord(i)+d
            if v > 90:
                v -= 26
            if v < 65:
                v += 26
            print(chr(v), end="")
        else:
            print(i, end="")
    print()
