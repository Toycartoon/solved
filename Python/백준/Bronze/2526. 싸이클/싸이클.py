n, p = map(int, input().split())
v = n
a = []
while True:
    a.append(v)
    v = (v * n) % p
    if v in a:
        break

print(len(a[a.index(v):]))
