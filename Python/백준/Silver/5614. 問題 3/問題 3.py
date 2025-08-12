w = {}
for i in range(int(input())):
    a, n = input().split()

    if a in w:
        w[a] += int(n)
    else:
        w[a] = int(n)

for i in sorted(w.keys(), key=lambda x: (len(x), x)):
    print(i, w[i])
