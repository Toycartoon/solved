t = 1
while True:
    n = int(input())
    if n <= 0:
        break

    my, mx = 0, 0
    mi = 0
    for i in range(n):
        x, y, m = map(int, input().split())
        mx += x * m
        my += y * m
        mi += m

    _ = input()
    print(f"Case {t}: {mx / mi:.02f} {my / mi:.02f}")
    t += 1
