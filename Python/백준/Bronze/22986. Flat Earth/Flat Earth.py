for t in range(int(input())):
    n, k = map(int, input().split())
    a = (n * (n+1) // 2) - ((n-k) * (n-k-1) // 2 if k <= n else 0)
    print(a * 4)
