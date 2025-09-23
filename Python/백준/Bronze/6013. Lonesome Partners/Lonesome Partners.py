a = []
for i in range(int(input())):
    x, y = map(int, input().split())
    a.append((x, y))

mx = -1
u, v = -1, -1
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            continue

        d = (abs(a[i][0] - a[j][0]) + (abs(a[i][1] - a[j][1]))) ** 0.5
        if max(mx, d) == d:
            mx = d
            u, v = i+1, j+1

if u > v:
    u, v = v, u
print(u, v)
