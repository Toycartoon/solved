w = {}
for i in range(int(input())):
    s, c, d = input().split()
    if d in w:
        if w[d][0] < int(c):
            w[d] = (int(c), s)
    else:
        w[d] = (int(c), s)

print(len(w))
for v in sorted(w.values(), key=lambda x: (x[1])):
    print(v[1])
