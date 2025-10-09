for t in range(int(input())):
    com, s = input().split()
    i = 1
    while i < len(s)-1:
        if s[i] + s[i+1] == "\\n":
            print()
            i += 1
        else:
            print(s[i], end="")
        i += 1