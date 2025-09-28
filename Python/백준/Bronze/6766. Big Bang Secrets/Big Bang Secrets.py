k = int(input())
s = input()
for i in range(len(s)):
    w = (i + 1) * -3 - k
    v = ord(s[i]) + w
    while v < 65:
        v += 26
    print(chr(v), end="")
