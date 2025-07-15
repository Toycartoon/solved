w = {}
for i in range(int(input())):
    n = int(input())
    if n in w:
        w[n] += 1
    else:
        w[n] = 1

print(max(w.values()))
