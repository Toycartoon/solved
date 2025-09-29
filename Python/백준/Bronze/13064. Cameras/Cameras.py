for i in range(int(input())):
    s = input()
    if len(s) != 8 or "0" in s:
        continue

    if s[0] == s[1] and s[0].isdigit() and s[2:4].isdigit() and s[4].isupper() and s[5:].isdigit():
        print(s)
