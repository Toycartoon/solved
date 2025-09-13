s = input()
a = []
for i in range(int(input())):
    x = input()
    l = s.count("L") + x.count("L")
    o = s.count("O") + x.count("O")
    v = s.count("V") + x.count("V")
    e = s.count("E") + x.count("E")

    p = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
    a.append((p, x))

a.sort(key=lambda x: (-x[0], x[1]))
print(a[0][1])
