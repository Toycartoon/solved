s = input()
ans = 0

v = 0
for i in s:
    if i.isupper():
        ans += (4 - (v % 4)) if v % 4 != 0 else 0
        v = 0
    v += 1
print(ans)
