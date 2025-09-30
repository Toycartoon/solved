c = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]

s = 0
for i in range(int(input())):
    a = int(input())
    s += a
    c[a] -= 1

x = 21-s
mn, mx = 0, 0
for i in range(len(c)):
    if i <= x:
        mn += c[i]
    else:
        mx += c[i]

if mn <= mx:
    print("DOSTA")
else:
    print("VUCI")
