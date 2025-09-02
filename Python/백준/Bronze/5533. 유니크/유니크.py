n = int(input())
a = []
s = [0 for _ in range(n)]
for _ in range(n):
    i, j, k = map(int, input().split())
    a.append((i, j, k))

for v in zip(*a):
    for i in range(n):
        if v.count(v[i]) == 1:
            s[i] += v[i]

for i in s:
    print(i)
