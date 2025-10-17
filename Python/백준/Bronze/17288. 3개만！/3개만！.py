s = input()
ans = 0
v = 1
for i in range(1, len(s)):
    if int(s[i-1]) + 1 == int(s[i]):
        v += 1
    else:
        if v == 3:
            ans += 1
        v = 1
if v == 3:
    ans += 1
print(ans)
