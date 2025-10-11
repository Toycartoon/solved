while True:
    n, c, k = map(int, input().split())
    if n == c == k == 0:
        break

    a = [0 for _ in range(k)]
    for _ in range(n):
        v = list(map(int, input().split()))
        for i in v:
            a[i-1] += 1

    mn = min(a)
    for i in range(k):
        if mn == a[i]:
            print(i+1, end=" ")
    print()
