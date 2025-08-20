from math import pi, trunc

for t in range(int(input())):
    r, a, b = map(int, input().split())

    ans = 0
    while True:
        ans += pi * r ** 2
        r *= a
        ans += pi * r ** 2
        r = trunc(r / b)
        if r == 0:
            break

    print(f"Case #{t+1}: {ans}")
