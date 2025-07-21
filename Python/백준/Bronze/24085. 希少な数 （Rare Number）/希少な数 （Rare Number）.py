n = int(input())
a = list(map(int, input().split()))

w = {}
for i in a:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

print(sorted(w.items(), key=lambda x: (x[1], x[0]))[0][0])
