a = []
for i in range(int(input())):
    g, s, b, *name = input().split()
    a.append((int(g), int(s), int(b), " ".join(name)))

a.sort(key=lambda x: (-x[0], -x[1], -x[2]))
print(a[0][-1])
