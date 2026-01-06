n = int(input())
s = input()

v = ""
f = True
idx = 0
while idx < n:
    if s[idx] not in "PAUL":
        if idx + 1 < n and s[idx+1] not in "PAUL":
            idx += 1
        else:
            f = False
            break
    else:
        v += s[idx]
    idx += 1

if v == "PAUL" and f:
    print("YES")
else:
    print("NO")
