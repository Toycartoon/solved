n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

a.sort()
print(sum(a) / n)
print(a[n // 2] if n % 2 == 1 else (a[n // 2] + a[n // 2 - 1]) / 2)
