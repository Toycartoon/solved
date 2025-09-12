x = int(input())
s = int(input())
i = int(input())

ans = 0
if s:
    ans += x
    if i:
        ans += int(input())
else:
    if i:
        for i in range(x):
            ans += int(input())

print(ans)
