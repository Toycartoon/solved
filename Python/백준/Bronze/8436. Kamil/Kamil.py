s = input()
ans = 1
for i in s:
    if i in ("T", "D", "L", "F"):
        ans *= 2
print(ans)
