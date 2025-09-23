n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

ans = float('inf')
for i in range(n):
    d = 0
    for j in range(n):
        if i == j:
            continue
        d += ((a[j][0]-a[i][0]) ** 2 + (a[j][1]-a[i][1]) ** 2) ** 0.5
    ans = min(ans, d / (n-1))
print(ans)
