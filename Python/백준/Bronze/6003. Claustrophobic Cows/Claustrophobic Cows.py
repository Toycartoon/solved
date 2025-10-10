a = []
for i in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y))

d = float('inf')
ans = (-1, -1)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        v = ((a[i][0]-a[j][0]) ** 2 + (a[i][1]-a[j][1]) ** 2) ** 0.5
        if d > v:
            d = v
            ans = (i+1, j+1)
print(*ans)
