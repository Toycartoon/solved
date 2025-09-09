a, b, c, d = map(int, input().split())
ans = []
for x in range(1, 4):
    if a ** x + b ** x + c ** x == d:
        ans.append(x)

if len(ans) != 1:
    print(-1)
else:
    print(ans[0])
