while True:
    n, t1, t2, t3 = map(int, input().split())
    if n == t1 == t2 == t3 == 0:
        break

    ans = 4 * n - 1
    ans += t2-t1
    if t1 > t2:
        ans += n

    ans += t2-t3
    if t2 < t3:
        ans += n

    print(ans)
