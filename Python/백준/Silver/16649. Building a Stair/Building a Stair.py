from math import ceil

n = int(input())

if n == 2:
    print(-1)
    exit()

print(ceil(n / 2))
if n % 2 == 1:
    for i in range(n // 2):
        print("o" + "." * (n // 2))
    print("o" * ceil(n / 2))
else:
    for i in range(n // 2 - 2):
        print("o" + "." * (n // 2 - 1))
    print("oo" + "." * (n // 2 - 2))
    print("o" * ceil(n / 2))
