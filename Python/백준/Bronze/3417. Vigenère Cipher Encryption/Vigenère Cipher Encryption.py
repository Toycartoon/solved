while True:
    p = input()
    if p == "0":
        break

    s = input()
    for i in range(len(s)):
        v = ord(s[i]) + (ord(p[i%len(p)])-64)
        print(chr(v) if v <= 90 else chr(v-26), end="")
    print()
