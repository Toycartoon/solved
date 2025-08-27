from math import ceil

while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break

    if ceil(n / 2) <= k:
        print(-1)
        continue

    print(max(ceil((n+1) / 2) - m, 0))
