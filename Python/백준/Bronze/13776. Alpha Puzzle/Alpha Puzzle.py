s = ""
for i in range(int(input())):
    v = input()
    for x in v:
        if x.isspace():
            continue
        if x not in s:
            s += x
print(s)
