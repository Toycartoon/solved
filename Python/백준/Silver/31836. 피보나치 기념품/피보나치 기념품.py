n = int(input())
a = []
b = []
while n > 2:
    b.append(n)
    a.extend([n-1, n-2])
    n -= 3

if n == 2:
    a.append(1)
    b.append(2)

print(len(a))
print(*a)
print(len(b))
print(*b)
