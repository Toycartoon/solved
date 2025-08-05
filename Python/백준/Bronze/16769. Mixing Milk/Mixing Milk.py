v = []
a = []
for i in range(3):
    c, m = map(int, input().split())
    v.append(c)
    a.append(m)

for i in range(100):
    if i % 3 == 0:
        if a[1] + a[0] <= v[1]:
            a[1] += a[0]
            a[0] = 0
        else:
            n = v[1] - a[1]
            a[1] += n
            a[0] -= n
    elif i % 3 == 1:
        if a[1] + a[2] <= v[2]:
            a[2] += a[1]
            a[1] = 0
        else:
            n = v[2] - a[2]
            a[2] += n
            a[1] -= n
    else:
        if a[2] + a[0] <= v[0]:
            a[0] += a[2]
            a[2] = 0
        else:
            n = v[0] - a[0]
            a[0] += n
            a[2] -= n

print(*a, sep="\n")
