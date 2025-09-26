n = int(input())
a = 0
if n % 5 == 0:
    a = n // 5
elif n % 5 == 1:
    if n // 5 > 0:
        a = (n // 5) - 1 + 2
    else:
        a = -1
elif n % 5 == 2:
    if n // 5 > 1:
        a = (n // 5) - 2 + 4
    else:
        a = -1
elif n % 5 == 3:
    a = n // 5 + 1
else:
    if n // 5 > 0:
        a = (n // 5) - 1 + 3
    else:
        a = -1
print(a)
