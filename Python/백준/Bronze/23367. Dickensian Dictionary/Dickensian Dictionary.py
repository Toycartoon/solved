l = "qwertasdfgzxcvb"
r = "yuiophjklnm"
s = input()

f = True
v = True if s[0] in l else False
for i in s:
    if (v and i not in l) or (not v and i not in r):
        f = False
        break
    v = not v

print("yes" if f else "no")
