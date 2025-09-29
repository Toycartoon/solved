w = "ABCDEFG"
while True:
    s = input()
    if s == "#":
        break

    idx = w.index(s[0])
    f = True
    for i in range(1, len(s)):
        if s[i] not in (w[(idx + 2) % 7], w[(idx + 4) % 7], w[(idx + 6) % 7]):
            f = False
            break
        idx = w.index(s[i])

    if f:
        print("That music is beautiful.")
    else:
        print("Ouch! That hurts my ears.")
