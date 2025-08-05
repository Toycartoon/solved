s = input()
v = 0
for i in s:
    v += ord(i)

print(chr(v // len(s)))
