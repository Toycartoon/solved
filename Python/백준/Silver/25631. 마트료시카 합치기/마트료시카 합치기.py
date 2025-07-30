n = int(input())
a = list(map(int, input().split()))

w = {}
for i in a:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

print(max(w.values()))
