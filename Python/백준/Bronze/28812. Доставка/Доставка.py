n, c = map(int, input().split())
a = []
for i in range(n):
    p, d, v = map(int, input().split())
    a.append(p + d + v * c)

print(min(a))
