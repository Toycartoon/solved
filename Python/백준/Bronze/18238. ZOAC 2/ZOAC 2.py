s = input()
p = "A"

ans = 0
for i in s:
    mx = max(ord(p), ord(i))
    mn = min(ord(p), ord(i))
    ans += min(mx-mn, (mn-mx)+26)
    p = i

print(ans)
