w = {}
n = int(input())
for i in range(n):
    s = input().split(".")[1]
    if s in w:
        w[s] += 1
    else:
        w[s] = 1

for i in sorted(w.items(), key=lambda x: x[0]):
    print(*i)
