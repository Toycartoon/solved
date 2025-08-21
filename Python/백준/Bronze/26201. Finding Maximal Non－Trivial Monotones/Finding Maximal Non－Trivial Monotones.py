n = int(input())
s = input().split("b")

ans = 0
for i in s:
    if len(i) != 1:
        ans += len(i)

print(ans)
