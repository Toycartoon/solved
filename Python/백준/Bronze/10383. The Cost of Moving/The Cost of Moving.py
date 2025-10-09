t = 1
while True:
    n = int(input())
    if n == 0:
        break

    s = []
    while len(s) < n:
        s.extend(input().split())

    v = sorted(s)
    ans = 0
    for i in range(n):
        ans += abs(i-s.index(v[i]))

    print(f"Site {t}: {ans}")
    t += 1
