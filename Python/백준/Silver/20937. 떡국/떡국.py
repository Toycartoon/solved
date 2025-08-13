n = int(input())
c = list(map(int, input().split()))

w = {}
for i in c:
    if i in w:
        w[i] += 1
    else:
        w[i] = 1

print(max(w.values()))
