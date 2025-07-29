for a in range(100, 1000):
    if a % 111 == 0:
        continue
    for b in range(100, 1000):
        if b % 100 != 0 and a % 10 == b // 100 and a / b == (a // 10) / (b % 100):
            print(f"{a} / {b} = {a // 10} / {b % 100}")
