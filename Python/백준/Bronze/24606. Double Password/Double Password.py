a = input()
b = input()
ans = 1
for i in range(4):
    if a[i] != b[i]:
        ans *= 2

print(ans)
