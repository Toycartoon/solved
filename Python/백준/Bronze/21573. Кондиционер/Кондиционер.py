troom, tcond = map(int, input().split())
s = input()

if s == "freeze":
    print(min(troom, tcond))
elif s == "heat":
    print(max(troom, tcond))
elif s == "auto":
    print(tcond)
elif s == "fan":
    print(troom)
