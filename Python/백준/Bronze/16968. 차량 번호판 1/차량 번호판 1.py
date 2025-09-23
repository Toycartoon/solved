s = input()
ans = 1
if s[0] == "d":
    ans *= 10
else:
    ans *= 26

for i in range(1, len(s)):
    if s[i] == "d":
        if s[i-1] == "d":
            ans *= 9
        else:
            ans *= 10
    elif s[i] == "c":
        if s[i-1] == "c":
            ans *= 25
        else:
            ans *= 26
print(ans)
