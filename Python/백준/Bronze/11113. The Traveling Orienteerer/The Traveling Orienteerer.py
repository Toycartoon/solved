a = []
for i in range(int(input())):
    x, y = map(float, input().split())
    a.append((x, y))

for t in range(int(input())):
    v = int(input())
    p = list(map(int, input().split()))
    d = 0
    for i in range(1, len(p)):
        d += ((a[p[i-1]][0]-a[p[i]][0]) ** 2 + (a[p[i-1]][1]-a[p[i]][1]) ** 2) ** 0.5
    print(round(d))
