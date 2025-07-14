n = int(input())
g = []
for i in range(n):
    j, p = map(int, input().split())
    g.append((j / p, p, i+1))

g.sort(key=lambda x: -x[0])
s = 0
for i in range(3):
    s += g[i][1]

print(s)
[print(g[i][2]) for i in range(3)]
