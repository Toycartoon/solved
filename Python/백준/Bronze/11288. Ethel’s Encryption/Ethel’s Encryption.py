n, a, b = map(int, input().split())
s = input()
for i in s:
    if i.isalpha():
        v = ord(i)-(pow(a, b, 26))
        if v < 65:
            v += 26
        print(chr(v), end="")
    else:
        print(i, end="")
