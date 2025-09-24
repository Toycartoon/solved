s = input()
a = input()

ans = 0
for i in range(len(a), len(s)+1):
    f = True
    p = s[i-len(a):i]
    for x in range(len(a)):
        if a[x] == p[x]:
            f = False
            break
    if f:
        ans += 1
print(ans)
