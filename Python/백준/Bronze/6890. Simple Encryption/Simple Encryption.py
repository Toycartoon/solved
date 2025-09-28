k = input()
x = input()
s = ""
for i in x:
    if i.isalpha():
        s += i

for i in range(len(s)):
    v = ord(s[i]) + (ord(k[i%len(k)])-65)
    if v > 90:
        v -= 26
    print(chr(v), end="")
