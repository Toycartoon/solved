k, s = map(int, input().split())
a = input()
for i in a:
    if i.isupper():
        x = ord(i) + (k % 26)
        if x > 90:
            x -= 26
        print(chr(x), end="")
    elif i.islower():
        x = ord(i) + (k % 26)
        if x > 122:
            x -= 26
        print(chr(x), end="")
    else:
        print(i, end="")
