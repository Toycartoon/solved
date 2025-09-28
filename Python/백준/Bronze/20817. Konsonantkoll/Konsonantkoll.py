s = input()
for i in range(len(s)):
    if i >= 2 and s[i] in "bcdfghjklmnpqrstvwxz" and s[i-2] == s[i-1] == s[i]:
        continue
    else:
        print(s[i], end="")
