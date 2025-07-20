s = {}
for i in range(int(input())):
    x = input().strip()
    if x in s:
        s[x] += 1
    else:
        s[x] = 1

ans = 0
for i in s.values():
    if i > 1:
        ans += 1

print(ans)
