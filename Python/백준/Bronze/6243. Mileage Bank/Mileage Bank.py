from math import ceil

ans = 0
while True:
    s = input()
    if s == "0":
        print(ans)
        ans = 0
        continue
    elif s == "#":
        break
    oc, dc, am, cc = s.split()
    if cc == "F":
        ans += int(am) * 2
    elif cc == "B":
        ans += int(am) + ceil(int(am) / 2)
    elif cc == "Y":
        if int(am) <= 500:
            ans += 500
        else:
            ans += int(am)
