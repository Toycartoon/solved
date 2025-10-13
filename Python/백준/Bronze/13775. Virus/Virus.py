n = int(input())
s = input()
for i in s:
    if i.isalpha():
        v = ord(i)-(n % 26)
        if v < 97:
            v += 26
        print(chr(v), end="")

        n += 1
        if n == 26:
            n = 1
    else:
        print(i, end="")
