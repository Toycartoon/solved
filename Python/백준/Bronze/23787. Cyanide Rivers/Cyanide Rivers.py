from math import ceil

s = input()
ans = []
v = 0
for i in range(len(s)):
    if s[i] == "0":
        v += 1
    else:
        ans.append(ceil(v / 2))
        v = 0
print(max(ans))
