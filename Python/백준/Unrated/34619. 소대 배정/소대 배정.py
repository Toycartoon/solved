from math import ceil

a, b, n, k = map(int, input().split())
v = []
for i in range(1, a+1):
    for j in range(1, b+1):
        v.append((i, j))
print(*v[ceil(k / n)-1])
