w = "VWXYZABCDEFGHIJKLMNOPQRSTU"
while True:
    s = input()
    if s == "START" or s == "END":
        continue
    if s == "ENDOFINPUT":
        break

    for i in s:
        if i.isalpha():
            print(w[ord(i)-65], end="")
        else:
            print(i, end="")
    print()
