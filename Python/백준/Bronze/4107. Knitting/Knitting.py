while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break

    a = list(map(int, input().split()))
    ans = n
    for i in range(m-1):
        n += a[i % k]
        ans += n
    print(ans)
