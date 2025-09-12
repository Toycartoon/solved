t = 1
while True:
    z = int(input())
    if z == 0:
        break

    ans = 0
    m = [0, 0, 0]
    for i in range(z):
        c, b, l, n = map(int, input().split())
        m = [m[0] + c, m[1] + b, m[2] + l]
        ans += c * 0.8 + b + l * 1.2 + n * 0.6

    ans -= m[0] * (7.5 / 85) + m[1] * (24 / 85) + m[2] * (32 / 85) + sum(m) * (8 / 85)
    print(f"Case #{t}: RM{ans:.02f}")
    t += 1
