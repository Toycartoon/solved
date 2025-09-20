n, s = input().split()
for i in range(int(n)):
    x = ord(s[i]) + pow(2, i, 26)
    if x > 90:
        x -= 26
    print(chr(x), end="")