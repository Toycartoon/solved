a, b = input().split()

ans = ""
for i in range(min(len(a), len(b))):
    if i % 2 == 0:
        ans += a[i]
    else:
        ans += b[i]

print(ans)
