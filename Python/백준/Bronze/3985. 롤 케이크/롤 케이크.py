l = int(input())
a = [0 for _ in range(l+1)]

v = []
for i in range(int(input())):
    p, k = map(int, input().split())
    v.append((k-p+1, i+1))
    for x in range(p, k+1):
        if a[x] == 0:
            a[x] = i+1

w = {}
for i in a:
    if i == 0:
        continue

    if i not in w:
        w[i] = 1
    else:
        w[i] += 1

v.sort(key=lambda x: (-x[0], x[1]))
print(v[0][1])
print(sorted(w.items(), key=lambda x: (-x[1], x[0]))[0][0])
