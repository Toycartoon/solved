a = []
for i in range(int(input())):
    x, y, r = map(int, input().split())
    a.append((x, y, r))

for i in range(len(a)):
    ans = 0
    for j in range(len(a)):
        if i == j:
            continue

        d = ((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2) ** 0.5
        if d < a[i][2] + a[j][2]:
            ans += 1
    print(ans)
