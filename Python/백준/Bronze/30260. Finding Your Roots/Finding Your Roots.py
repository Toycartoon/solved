for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 1
    while a[n-1] != 0:
        n = a[n-1]
        ans += 1

    print(f"Data Set {t+1}:")
    print(ans)
    print()
