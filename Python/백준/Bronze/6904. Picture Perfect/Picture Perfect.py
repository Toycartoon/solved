while True:
    n = int(input())
    if n == 0:
        break

    a, b = 1, n
    for i in range(1, (n // 2)+1):
        if n % i != 0:
            continue
        if i * 2 + (n // i) * 2 < a * 2 + b * 2:
            a, b = i, n // i

    if a > b:
        a, b = b, a
    print(f"Minimum perimeter is {a * 2 + b * 2} with dimensions {a} x {b}")
