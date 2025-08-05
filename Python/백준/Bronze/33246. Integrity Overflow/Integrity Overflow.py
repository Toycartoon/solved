n = int(input())
s = input()
f = True
for i in range(n):
    p = True
    d = False
    x, r = input().split()

    if len(x) != len(s):
        if r == "ALLOWED":
            f = False
            break
        continue

    for v in range(len(s)):
        if s[v] != x[v]:
            if p:
                p = False
            else:
                if r == "ALLOWED":
                    f = False
                d = True
                break

    if (d and r == "ALLOWED") or (not d and r == "DENIED"):
        f = False

    if not f:
        break

if f:
    print("SYSTEM SECURE")
else:
    print("INTEGRITY OVERFLOW")
