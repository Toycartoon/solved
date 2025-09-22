while True:
    s = input()
    if s == "end":
        break

    f = True
    if len({*s} - {*"aeiou"}) == len(s):
        f = False

    for i in range(2, len(s)):
        if (s[i-2] not in "aeiou" and s[i-1] not in "aeiou" and s[i] not in "aeiou") or (s[i-2] in "aeiou" and s[i-1] in "aeiou" and s[i] in "aeiou"):
            f = False
            break

    for i in range(1, len(s)):
        if s[i-1] == s[i] and not (s[i] == "e" or s[i] == "o"):
            f = False
            break

    if f:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")
