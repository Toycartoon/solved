lx, ly = map(int, input().split())
n = int(input())
k = input()

x, y = 0, 0
ans = []
for i in range(n):
    if abs(lx-x) <= 1 and abs(ly-y) <= 1:
        ans.append(i)

    if k[i] == "I":
        x += 1
    elif k[i] == "Z":
        x -= 1
    elif k[i] == "S":
        y += 1
    elif k[i] == "J":
        y -= 1

if abs(lx-x) <= 1 and abs(ly-y) <= 1:
    ans.append(n)

if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)
