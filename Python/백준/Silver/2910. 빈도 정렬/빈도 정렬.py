n, c = map(int, input().split())
a = list(map(int, input().split()))

w = {}
for i in a:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

for i in sorted(w.items(), key=lambda x: (-x[1])):
    print((str(i[0]) + " ") * i[1], end="")
