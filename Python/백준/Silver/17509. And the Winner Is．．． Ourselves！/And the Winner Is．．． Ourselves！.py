a = []
for i in range(11):
    d, v = map(int, input().split())
    a.append((d, v))

a.sort()
t = 0
p = 0
for d, v in a:
    t += d
    p += t + 20 * v
print(p)
