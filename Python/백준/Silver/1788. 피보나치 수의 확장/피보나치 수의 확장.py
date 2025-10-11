n = int(input())
f, g = 0, 1
for i in range(abs(n)):
    if i % 2 == 0:
        f += g
        f %= 1000000000
    else:
        g += f
        g %= 1000000000

if n < 0 and n % 2 == 0:
    print(-1)
    print(f if n % 2 == 0 else g)
elif n > 0 or (n < 0 and n % 2 == 1):
    print(1)
    print(f if n % 2 == 0 else g)
else:
    print(0)
    print(0)
