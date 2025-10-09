t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        a.append(input())

    print(f"SET {t}")
    for i in range(0, n, 2):
        print(a[i])

    for i in range(n-2 if n % 2 == 1 else n-1, 0, -2):
        print(a[i])
    t += 1
