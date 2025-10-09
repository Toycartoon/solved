n, d = map(int, input().split())
a = []
for i in range(n // 2):
    a.append(d+i+1)
    a.append(d-(i+1))

if n % 2 == 1:
    a.append(d)
print(*a)
