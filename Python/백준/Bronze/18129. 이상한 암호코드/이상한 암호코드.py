a = set()
s, k = input().lower().split()

v = 1
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        v += 1
    else:
        if v >= int(k) and s[i-1] not in a:
            print(1, end="")
        elif v < int(k) and s[i-1] not in a:
            print(0, end="")
        v = 1
        a.add(s[i-1])

if v >= int(k) and s[-1] not in a:
    print(1, end="")
elif v < int(k) and s[-1] not in a:
    print(0, end="")
