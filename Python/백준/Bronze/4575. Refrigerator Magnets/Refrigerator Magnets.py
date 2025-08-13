while True:
    s = input()
    if s == "END":
        break

    w = {}
    for i in s:
        if not i.isalpha():
            continue

        if i in w:
            w[i] += 1
        else:
            w[i] = 1

    if min(w.values()) == max(w.values()) == 1:
        print(s)
