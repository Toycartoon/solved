n = int(input())
a, b = 0, 0

f = True
while n != 0:
    i = n // 2 if n % 2 == 0 else n // 2 + 1
    j = n - i

    if f:
        b += i
        n = j
    else:
        a += i
        n = j

    f = not f

print(a, b)
