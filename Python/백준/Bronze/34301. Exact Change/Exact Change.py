n = int(input())
a = []
for i in (150, 30, 15, 5, 1):
    a.append(n // i)
    n %= i

print(*a[::-1])
