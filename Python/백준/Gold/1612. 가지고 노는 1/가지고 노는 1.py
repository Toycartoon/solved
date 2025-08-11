n = int(input())
i = 1
if n % 2 == 0 or n % 5 == 0:
    print(-1)
    exit(0)

a = 1
while True:
    if a % n == 0:
        print(i)
        break

    a = 10 * a + 1
    a %= n
    i += 1
