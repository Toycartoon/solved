q = 0
s = input()

ans = 0
for i in range(len(s)):
    if s[i] == "(":
        q += 1
    elif s[i] == ")":
        q -= 1
        if s[i-1] == "(":
            ans += q
        else:
            ans += 1

print(ans)
