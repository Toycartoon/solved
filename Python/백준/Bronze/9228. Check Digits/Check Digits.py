while True:
    n = input()
    if n == "#":
        break

    s = 0
    n = n[::-1]
    for i in range(len(n)):
        s += int(n[i]) * (i+2)
    print(f"{n[::-1]} -> {0 if s % 11 == 0 else (11 - (s % 11)) if 11 - (s % 11) != 10 else "Rejected"}")
