n = int(input())
a, b = 0, n // 3
if n % 3 == 1:
    b -= 1
    a += 2
elif n % 3 == 2:
    a += 1

print(a, b)
