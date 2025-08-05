n = int(input())
a = list(map(int, input().split()))

ans = []
x = 0
for i in a:
    if i == 1:
        x += 1
    else:
        ans.append(x)
        x = 0

ans.append(x)
print(max(ans) + 1)
