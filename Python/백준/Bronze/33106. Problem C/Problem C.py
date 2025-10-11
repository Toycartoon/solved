for t in range(int(input())):
    s = [*input()]
    for i in range(len(s)):
        if s[i] != "c":
            continue

        if i+1 < len(s) and s[i+1] in "eiy":
            s[i] = "s"
        elif i+1 < len(s) and s[i+1] == "h":
            s[i+1] = ""
        else:
            s[i] = "k"
    print(*s, sep="")
