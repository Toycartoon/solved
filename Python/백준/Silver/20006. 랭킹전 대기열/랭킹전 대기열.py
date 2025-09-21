p, m = map(int, input().split())
a = []
for i in range(p):
    l, n = input().split()
    f = True
    l = int(l)
    for i in range(len(a)):
        if abs(a[i][0][0]-l) <= 10 and len(a[i]) < m:
            a[i].append((l, n))
            f = False
            break
    if f:
        a.append([(l, n)])

for i in a:
    if len(i) == m:
        print("Started!")
    else:
        print("Waiting!")

    i.sort(key=lambda x: x[1])
    for v in i:
        print(*v)
