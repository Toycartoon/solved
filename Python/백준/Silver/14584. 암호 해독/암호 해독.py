s = input()
a = []
for i in range(int(input())):
    a.append(input())

for d in range(26):
    txt = ""
    for i in s:
        v = ord(i)+d
        if v > 122:
            v -= 26
        txt += chr(v)

    f = False
    for i in a:
        if i in txt:
            f = True
            break

    if f:
        print(txt)
        break
