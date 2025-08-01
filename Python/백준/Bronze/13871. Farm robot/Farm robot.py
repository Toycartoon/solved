n, c, s = map(int, input().split())
x = list(map(int, input().split()))

g = [0 for _ in range(n)]

g[1] = 1
v = 1
for i in x:
    v += i
    v %= n
    g[v] += 1

print(g[s] if s != n else g[0])
