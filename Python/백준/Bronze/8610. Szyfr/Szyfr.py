a = [0 for _ in range(26)]
n, c = input().split()
s = input()
for i in s:
    if i.isalpha():
        a[ord(i)-65] += 1

d = (ord(c)-65)-a.index(max(a))
if d > 0:
    d -= 26

for i in s:
    if i.isalpha():
        v = ord(i)+d
        if v > 90:
            v -= 26
        if v < 65:
            v += 26
        print(chr(v), end="")
    else:
        print(i, end="")
