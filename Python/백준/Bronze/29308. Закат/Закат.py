n = int(input())
g = []
for i in range(n):
    m, p, c = input().split()
    if c == "Russia":
        g.append((int(m), p))

g.sort(key=lambda x: -x[0])
print(g[0][1])
