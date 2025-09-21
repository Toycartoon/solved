w = [0 for _ in range(26)]
s = input()
for i in s:
    w[ord(i)-65] += 1

a = input()
f = True
for i in a:
    if w[ord(i)-65] > 0:
        w[ord(i)-65] -= 1
    else:
        f = False
        break

if f:
    print("OK")
else:
    print("NEED FIX")
