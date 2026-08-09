n = int(input())

a = 1
while True:
    for b in range(int((n + a ** 2) ** 0.5), 0, -1):
        c = (n - b * a) // (a + b)
        if a * b + b * c + c * a == n and 4 + a + b + c <= 10 ** 6:
            print(4 + a + b + c)
            for i in range(3):
                print(1, i+2)

            for i in range(a):
                print(2, 5+i)

            for i in range(b):
                print(3, 5+a+i)

            for i in range(c):
                print(4, 5+a+b+i)
            exit()
    a += 1
