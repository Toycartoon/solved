w = {}
for i in range(int(input())):
    s = input().split()
    if len(s) in w:
        w[len(s)] += 1
    else:
        w[len(s)] = 1

for v in sorted(w.keys()):
    print(v, w[v])
