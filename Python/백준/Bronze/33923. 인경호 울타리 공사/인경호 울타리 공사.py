n, m = map(int, input().split())
if n != m:
    print(min(n-1, m-1) ** 2)
else:
    print((n-2) ** 2 + 1)
