m, n = map(int, input().split())
a = []
for i in range(n):
    v = m // n + m % n
    a.append(v)
    m -= v
print(*a)
print(m)
