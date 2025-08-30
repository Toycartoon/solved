n, m, k = map(int, input().split())
if m >= k:
    print(n * ((k-1) + m // k))
else:
    print(n * m)
