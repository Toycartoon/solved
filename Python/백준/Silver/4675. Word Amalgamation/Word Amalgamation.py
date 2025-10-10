w = {}
while True:
    s = input()
    if s == "XXXXXX":
        break
    if tuple(sorted([*s])) in w:
        w[tuple(sorted([*s]))].append(s)
    else:
        w[tuple(sorted([*s]))] = [s]

while True:
    s = input()
    if s == "XXXXXX":
        break

    if tuple(sorted([*s])) in w:
        for i in sorted(w[tuple(sorted([*s]))]):
            print(i)
    else:
        print("NOT A VALID WORD")
    print("******")
