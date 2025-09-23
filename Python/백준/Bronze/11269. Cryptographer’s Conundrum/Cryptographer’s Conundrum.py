s = input()
x = "PER"

ans = 0
for i in range(len(s)):
    if s[i] != x[i % 3]:
        ans += 1
print(ans)
