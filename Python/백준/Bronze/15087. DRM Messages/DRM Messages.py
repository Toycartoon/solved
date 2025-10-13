s = input()
l, r = s[:len(s)//2], s[len(s)//2:]

ls, rs = 0, 0
for i in l:
    ls += ord(i)-65

for i in r:
    rs += ord(i)-65

ls %= 26
rs %= 26
nl, nr = "", ""
for i in l:
    v = ord(i)+ls
    if v > 90:
        v -= 26
    nl += chr(v)

for i in r:
    v = ord(i)+rs
    if v > 90:
        v -= 26
    nr += chr(v)

ans = ""
for i in range(len(nl)):
    v = ord(nl[i]) + (ord(nr[i])-65)
    if v > 90:
        v -= 26
    ans += chr(v)
print(ans)
