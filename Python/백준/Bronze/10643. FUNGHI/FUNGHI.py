a = []
for i in range(8):
    a.append(int(input()))

a *= 2
ans = 0
for i in range(4, 16):
    ans = max(ans, sum(a[i-4:i]))
print(ans)
