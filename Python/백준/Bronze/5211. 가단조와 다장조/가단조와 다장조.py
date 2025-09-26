s = input().split("|")
a, c = 0, 0
for i in s:
    if i[0] in "ADE":
        a += 1
    elif i[0] in "CFG":
        c += 1

if a > c:
    print("A-minor")
elif c > a:
    print("C-major")
else:
    if s[-1][-1] in "ADE":
        print("A-minor")
    elif s[-1][-1] in "CFG":
        print("C-major")
