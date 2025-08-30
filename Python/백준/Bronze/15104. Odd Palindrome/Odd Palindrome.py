s = input()
f = True
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        f = False
        break

if f:
    print("Odd.")
else:
    print("Or not.")
