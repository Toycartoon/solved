t = 1
while True:
    n = int(input())
    if n == 0:
        break

    a = []
    for i in range(n):
        d, p = map(int, input().split())
        a.append((p / (d ** 2), d))
    a.sort()
    print(f"Menu {t}: {a[0][1]}")

    t += 1
