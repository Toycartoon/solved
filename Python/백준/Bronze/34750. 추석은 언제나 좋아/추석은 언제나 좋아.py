n = int(input())
if n >= 1000000:
    print(int(n * 0.2), int(n - n * 0.2))
elif n >= 500000:
    print(int(n * 0.15), int(n - n * 0.15))
elif n >= 100000:
    print(int(n * 0.1), int(n - n * 0.1))
else:
    print(int(n * 0.05), int(n - n * 0.05))
