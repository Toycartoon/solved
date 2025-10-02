n = int(input())
a = []
if n % 2 == 1:
    a.append(3)
    n -= 3

a.extend([2] * (n // 2))
print(len(a))
print(*a)
