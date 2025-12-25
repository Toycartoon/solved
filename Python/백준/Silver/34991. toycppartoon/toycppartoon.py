s = input()
ans = "toycartoon"

if s in ans:
    print(ans)
    exit()

t, o = -1, 0
for i in range(len(s)):
    if s[:i+1] not in ans:
        t = ans.index(s[:i])
        break
    else:
        o += 1

if o == 0:
    print(ans if len(ans + f"_{s}") > 20 else ans + f"_{s}")
    exit()

y = ans[t+o:]
for i in range(len(s)-1, o-1, -1):
    if ans[t+o:].startswith(s[i:]):
        y = ans[t+o+len(s[i:]):]

ans = ans[:t] + s + y
print(ans if len(ans) <= 20 else "toycartoon")
