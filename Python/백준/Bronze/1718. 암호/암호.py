s = input()
k = input()
for i in range(len(s)):
    if s[i].isalpha():
        x = ord(s[i])-(ord(k[i % len(k)])-97)-1
        if x < 97:
            x += 26
        print(chr(x), end="")
    else:
        print(s[i], end="")