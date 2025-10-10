d = int(input())
n = 360
while True:
    if n % d == 0:
        print(n // d)
        break
    n += 360
