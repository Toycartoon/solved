s = input()
s = s[4:] + s[:4]

v = ""
for i in s:
    if i.isalpha():
        v += str(ord(i)-55)
    else:
        v += i

if int(v) % 97 == 1:
    print("correct")
else:
    print("incorrect")
