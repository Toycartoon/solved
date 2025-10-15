a = input()
b = input()
ans = 0
for l in range(len(a), -1, -1):
    if b.endswith(a[:l]):
        ans = max(ans, l)
        break

for l in range(len(b), -1, -1):
    if a.endswith(b[:l]):
        ans = max(ans, l)
        break
print(ans)
