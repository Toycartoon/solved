s = input()
ans = []
for l in range(len(s)):
    for r in range(l+1, len(s)+1):
        ans.append(s[l:r])

ans.sort(reverse=True)
print(ans[0])
