p = input()
s = input()

for i in s:
    if i.islower():
        print(p[ord(i)-97], end="")
    elif i.isupper():
        print(p[ord(i)-65].upper(), end="")
    else:
        print(i, end="")
