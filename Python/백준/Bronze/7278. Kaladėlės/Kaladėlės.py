n = int(input())
a = map(int, input().split())

r = []
for i in a:
    if abs(n - (n // i) * i) <= abs(n - (n // i + 1) * i):
        r.append((i, (n // i) * i))
    else:
        r.append((i, (n // i + 1) * i))
r.sort(key=lambda x: abs(n-x[1]))
print(*r[0])
