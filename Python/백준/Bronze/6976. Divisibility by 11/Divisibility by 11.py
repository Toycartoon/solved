for t in range(int(input())):
    s = int(input())
    n = s
    while s >= 100:
        print(s)
        s = s // 10 - s % 10

    print(s)
    print(f"The number {n} is{' not' if s % 11 != 0 else ''} divisible by 11.")
    print()
