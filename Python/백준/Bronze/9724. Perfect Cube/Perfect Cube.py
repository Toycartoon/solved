for t in range(int(input())):
    a, b = map(int, input().split())
    ans = 0

    x = 1
    while x ** 3 <= b:
        if a <= x ** 3 <= b:
            ans += 1
        x += 1

    print(f"Case #{t+1}: {ans}")
