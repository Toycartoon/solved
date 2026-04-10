from math import ceil

n = int(input())
a = list(map(int, input().split()))

ans = a.count(4)
o = a.count(1)
t = a.count(3)

o -= min(t, o)
ans += t

tw = a.count(2)
if tw % 2 == 0:
    ans += tw // 2
else:
    ans += tw // 2
    if o >= 2:
        o -= 2
    elif o >= 1:
        o -= 1
    ans += 1

ans += ceil(o / 4)
print(ans)
