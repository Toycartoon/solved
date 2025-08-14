w = {}
s = input().split()
for i in s:
    if i.startswith("#") and i.count("#") == 1 and len(i) >= 2:
        if i in w:
            w[i] += 1
        else:
            w[i] = 1

print(len(w))
for i in sorted(w.keys()):
    print(i, w[i])
