s = input()
ans = 1
v = 1
for i in range(1, len(s)):
    if s[i-1] < s[i]:
        v += 1
    else:
        v = 1
    ans += v
print(ans)
