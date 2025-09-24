s = input()
v = ""
for i in s:
    if i in "aeiou":
        v += i

if v == v[::-1]:
    print("S")
else:
    print("N")
